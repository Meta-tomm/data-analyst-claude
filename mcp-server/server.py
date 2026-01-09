#!/usr/bin/env python3
"""
Data Analyst MCP Server
Provides database connectivity tools for Claude Code

Tools:
- db_connect: Test database connection
- db_tables: List all tables in database
- db_schema: Get schema for a table
- db_query: Execute a SELECT query (read-only)
- db_profile: Profile a table (stats, nulls, types)
"""

import json
import os
import sys
from typing import Any
import asyncio

# MCP SDK
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Database drivers
try:
    import psycopg2
    import psycopg2.extras
    POSTGRES_AVAILABLE = True
except ImportError:
    POSTGRES_AVAILABLE = False

try:
    import mysql.connector
    MYSQL_AVAILABLE = True
except ImportError:
    MYSQL_AVAILABLE = False


class DatabaseConnection:
    """Manages database connections"""

    def __init__(self):
        self.connection = None
        self.db_type = None
        self.connected = False

    def connect_from_env(self) -> dict:
        """Connect using environment variables"""
        db_url = os.environ.get("DATABASE_URL") or os.environ.get("DB_URL")

        if db_url:
            return self.connect_from_url(db_url)

        # Try individual vars
        db_type = os.environ.get("DB_TYPE", "postgresql").lower()
        host = os.environ.get("DB_HOST", "localhost")
        port = os.environ.get("DB_PORT")
        database = os.environ.get("DB_NAME") or os.environ.get("DB_DATABASE")
        user = os.environ.get("DB_USER")
        password = os.environ.get("DB_PASSWORD")

        if not database:
            return {"success": False, "error": "No database configured. Set DATABASE_URL or DB_NAME"}

        return self.connect(db_type, host, port, database, user, password)

    def connect_from_url(self, url: str) -> dict:
        """Parse connection URL and connect"""
        # postgresql://user:pass@host:port/database
        # mysql://user:pass@host:port/database

        try:
            if url.startswith("postgresql://") or url.startswith("postgres://"):
                self.db_type = "postgresql"
                if not POSTGRES_AVAILABLE:
                    return {"success": False, "error": "psycopg2 not installed. Run: pip install psycopg2-binary"}
                self.connection = psycopg2.connect(url)

            elif url.startswith("mysql://"):
                self.db_type = "mysql"
                if not MYSQL_AVAILABLE:
                    return {"success": False, "error": "mysql-connector not installed. Run: pip install mysql-connector-python"}
                # Parse URL for mysql
                from urllib.parse import urlparse
                parsed = urlparse(url)
                self.connection = mysql.connector.connect(
                    host=parsed.hostname,
                    port=parsed.port or 3306,
                    database=parsed.path.lstrip('/'),
                    user=parsed.username,
                    password=parsed.password
                )
            else:
                return {"success": False, "error": f"Unsupported database URL scheme. Use postgresql:// or mysql://"}

            self.connected = True
            return {"success": True, "db_type": self.db_type}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def connect(self, db_type: str, host: str, port: str, database: str, user: str, password: str) -> dict:
        """Connect with individual parameters"""
        try:
            if db_type in ("postgresql", "postgres"):
                self.db_type = "postgresql"
                if not POSTGRES_AVAILABLE:
                    return {"success": False, "error": "psycopg2 not installed"}
                self.connection = psycopg2.connect(
                    host=host,
                    port=port or 5432,
                    database=database,
                    user=user,
                    password=password
                )
            elif db_type == "mysql":
                self.db_type = "mysql"
                if not MYSQL_AVAILABLE:
                    return {"success": False, "error": "mysql-connector not installed"}
                self.connection = mysql.connector.connect(
                    host=host,
                    port=int(port or 3306),
                    database=database,
                    user=user,
                    password=password
                )
            else:
                return {"success": False, "error": f"Unsupported database type: {db_type}"}

            self.connected = True
            return {"success": True, "db_type": self.db_type}

        except Exception as e:
            return {"success": False, "error": str(e)}

    def execute(self, query: str, params: tuple = None) -> list:
        """Execute a query and return results"""
        if not self.connected:
            raise Exception("Not connected to database")

        cursor = self.connection.cursor()
        cursor.execute(query, params)

        if cursor.description:
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            return [dict(zip(columns, row)) for row in rows]
        return []

    def close(self):
        if self.connection:
            self.connection.close()
            self.connected = False


# Global connection
db = DatabaseConnection()

# MCP Server
server = Server("data-analyst-db")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available database tools"""
    return [
        Tool(
            name="db_connect",
            description="Connect to database using environment variables (DATABASE_URL or DB_HOST/DB_NAME/etc)",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": []
            }
        ),
        Tool(
            name="db_tables",
            description="List all tables in the connected database",
            inputSchema={
                "type": "object",
                "properties": {
                    "schema": {
                        "type": "string",
                        "description": "Schema name (default: public for PostgreSQL, database for MySQL)"
                    }
                },
                "required": []
            }
        ),
        Tool(
            name="db_schema",
            description="Get schema (columns, types) for a specific table",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {
                        "type": "string",
                        "description": "Table name"
                    },
                    "schema": {
                        "type": "string",
                        "description": "Schema name (optional)"
                    }
                },
                "required": ["table"]
            }
        ),
        Tool(
            name="db_query",
            description="Execute a SELECT query (read-only). Returns up to 100 rows.",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "SQL SELECT query to execute"
                    }
                },
                "required": ["query"]
            }
        ),
        Tool(
            name="db_profile",
            description="Profile a table: row count, column stats, null counts, sample values",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {
                        "type": "string",
                        "description": "Table name to profile"
                    },
                    "schema": {
                        "type": "string",
                        "description": "Schema name (optional)"
                    }
                },
                "required": ["table"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls"""

    try:
        if name == "db_connect":
            result = db.connect_from_env()
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        # All other tools require connection
        if not db.connected:
            # Try auto-connect
            result = db.connect_from_env()
            if not result["success"]:
                return [TextContent(type="text", text=json.dumps(result, indent=2))]

        if name == "db_tables":
            schema = arguments.get("schema")
            result = get_tables(schema)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "db_schema":
            table = arguments["table"]
            schema = arguments.get("schema")
            result = get_table_schema(table, schema)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "db_query":
            query = arguments["query"]
            result = execute_query(query)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        elif name == "db_profile":
            table = arguments["table"]
            schema = arguments.get("schema")
            result = profile_table(table, schema)
            return [TextContent(type="text", text=json.dumps(result, indent=2))]

        else:
            return [TextContent(type="text", text=f"Unknown tool: {name}")]

    except Exception as e:
        return [TextContent(type="text", text=json.dumps({"error": str(e)}, indent=2))]


def get_tables(schema: str = None) -> dict:
    """Get list of tables"""
    if db.db_type == "postgresql":
        schema = schema or "public"
        query = """
            SELECT table_name, table_type
            FROM information_schema.tables
            WHERE table_schema = %s
            ORDER BY table_name
        """
        rows = db.execute(query, (schema,))
    else:  # mysql
        query = """
            SELECT table_name, table_type
            FROM information_schema.tables
            WHERE table_schema = DATABASE()
            ORDER BY table_name
        """
        rows = db.execute(query)

    return {"tables": rows, "count": len(rows)}


def get_table_schema(table: str, schema: str = None) -> dict:
    """Get table schema"""
    if db.db_type == "postgresql":
        schema = schema or "public"
        query = """
            SELECT
                column_name,
                data_type,
                is_nullable,
                column_default,
                character_maximum_length
            FROM information_schema.columns
            WHERE table_schema = %s AND table_name = %s
            ORDER BY ordinal_position
        """
        rows = db.execute(query, (schema, table))
    else:  # mysql
        query = """
            SELECT
                column_name,
                data_type,
                is_nullable,
                column_default,
                character_maximum_length
            FROM information_schema.columns
            WHERE table_schema = DATABASE() AND table_name = %s
            ORDER BY ordinal_position
        """
        rows = db.execute(query, (table,))

    return {"table": table, "columns": rows, "column_count": len(rows)}


def execute_query(query: str) -> dict:
    """Execute a SELECT query with safety checks"""
    # Safety: only allow SELECT
    query_upper = query.strip().upper()
    if not query_upper.startswith("SELECT"):
        return {"error": "Only SELECT queries are allowed for safety"}

    # Block dangerous keywords
    dangerous = ["DROP", "DELETE", "UPDATE", "INSERT", "ALTER", "TRUNCATE", "CREATE", "GRANT", "REVOKE"]
    for kw in dangerous:
        if kw in query_upper:
            return {"error": f"Query contains forbidden keyword: {kw}"}

    # Add LIMIT if not present
    if "LIMIT" not in query_upper:
        query = query.rstrip(";") + " LIMIT 100"

    rows = db.execute(query)
    return {"rows": rows, "row_count": len(rows)}


def profile_table(table: str, schema: str = None) -> dict:
    """Profile a table"""
    # Get row count
    full_table = f"{schema}.{table}" if schema else table

    count_result = db.execute(f"SELECT COUNT(*) as cnt FROM {full_table}")
    row_count = count_result[0]["cnt"] if count_result else 0

    # Get columns
    schema_info = get_table_schema(table, schema)
    columns = schema_info.get("columns", [])

    # Profile each column
    column_profiles = []
    for col in columns[:20]:  # Limit to 20 columns
        col_name = col["column_name"]
        col_type = col["data_type"]

        try:
            # Null count
            null_query = f"SELECT COUNT(*) as cnt FROM {full_table} WHERE {col_name} IS NULL"
            null_result = db.execute(null_query)
            null_count = null_result[0]["cnt"] if null_result else 0

            # Distinct count
            distinct_query = f"SELECT COUNT(DISTINCT {col_name}) as cnt FROM {full_table}"
            distinct_result = db.execute(distinct_query)
            distinct_count = distinct_result[0]["cnt"] if distinct_result else 0

            profile = {
                "column": col_name,
                "type": col_type,
                "null_count": null_count,
                "null_pct": round(100 * null_count / row_count, 2) if row_count > 0 else 0,
                "distinct_count": distinct_count
            }

            # Numeric stats
            if col_type in ("integer", "bigint", "smallint", "decimal", "numeric", "real", "double precision", "int", "float", "double"):
                stats_query = f"SELECT MIN({col_name}) as min_val, MAX({col_name}) as max_val, AVG({col_name}) as avg_val FROM {full_table}"
                stats = db.execute(stats_query)
                if stats:
                    profile["min"] = stats[0].get("min_val")
                    profile["max"] = stats[0].get("max_val")
                    profile["avg"] = round(float(stats[0].get("avg_val") or 0), 2)

            column_profiles.append(profile)
        except:
            column_profiles.append({"column": col_name, "type": col_type, "error": "Could not profile"})

    return {
        "table": table,
        "row_count": row_count,
        "column_count": len(columns),
        "columns": column_profiles
    }


async def main():
    """Run the MCP server"""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
