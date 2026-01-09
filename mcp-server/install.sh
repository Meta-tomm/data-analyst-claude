#!/bin/bash
# Install MCP server dependencies

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "Installing data-analyst MCP server dependencies..."

pip install -r "$SCRIPT_DIR/requirements.txt"

echo ""
echo "Installation complete!"
echo ""
echo "To use the database tools, set one of these environment variables:"
echo ""
echo "  Option 1: DATABASE_URL"
echo "    export DATABASE_URL='postgresql://user:password@localhost:5432/mydb'"
echo "    export DATABASE_URL='mysql://user:password@localhost:3306/mydb'"
echo ""
echo "  Option 2: Individual variables"
echo "    export DB_TYPE=postgresql  # or mysql"
echo "    export DB_HOST=localhost"
echo "    export DB_PORT=5432"
echo "    export DB_NAME=mydb"
echo "    export DB_USER=user"
echo "    export DB_PASSWORD=password"
echo ""
