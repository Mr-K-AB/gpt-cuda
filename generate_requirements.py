import subprocess

def generate_requirements_file(output_file='requirements.txt'):
    """Generate requirements.txt file with installed packages."""
    try:
        # Run pip freeze and capture the output
        with open(output_file, 'w') as f:
            subprocess.run(['pip', 'freeze'], stdout=f, check=True)
        print(f"{output_file} generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error generating {output_file}: {e}")

if __name__ == "__main__":
    generate_requirements_file()
