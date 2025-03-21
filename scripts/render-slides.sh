#!/bin/bash
# Generate cheatsheet based on YAML input

render_slides() {
    local escaped_file
    local filename
    local input_file

    # Remove any surrounding quotes from the variables
    input_file=${1//\"/}

    # Derive other necessary variables from the input_file
    filename=$(basename "$input_file")
    filename=${filename%.*}

    # Escape strings for sed
    escaped_file=$(printf '%s\n' "$input_file" | sed -e 's/[\/&$]/\\&/g')
    temp_slides_md=$(mktemp -u -p ./)

    # Create temporary markdown file using the slide template
    sed -e "s/<SRC>/$escaped_file/g" slides-template.md > "$temp_slides_md"

    docker run -it --rm --user "$(id -u)":"$(id -g)" \
      -v "$PWD:/repo" \
      -p 8000:8000 \
      mcr.microsoft.com/playwright:v1.50.0-noble \
      bash -c "cd /repo && npm run dev $temp_slides_md -- -o false -p 8000 --remote --force"

    # Clean up temporary markdown file
    rm "$temp_slides_md"
}

check_dependencies() {
  local dependencies=( yq )
  local return_value=0
  for dependency in "${dependencies[@]}"; do
    if ! command -v "$dependency" >/dev/null; then
      echo "$dependency is missing"
      return_value=1
    fi
  done
  return $return_value
}


error_exit() {
  print_error "$1"
  exit 1
}

print_usage_error() {
  print_help
  error_exit "$1"
}

print_error() {
  local red="\033[31m"
  local reset="\033[0m"
  echo -e "${red}ERROR: $1${reset}"
}

if ! check_dependencies; then
  error_exit "Missing dependencies"
fi

print_help() {
cat <<EOF
$(basename "$0") [OPTION]... [slides_filename]
EOF
}

if [ $# -ne 1 ]; then
  print_usage_error "Script accepts 1 positional arguments, got $#"
fi

# Call the function with the provided YAML file
render_slides "$1"
