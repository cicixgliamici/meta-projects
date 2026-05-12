# Build Systems and Build Tools

In the software development lifecycle, writing code is only the first step. For code to be executed by a machine, distributed to a client, or packaged into a Docker container, it must be **built**.

**Build Systems** are tools that automate this process. Their main job is to take source code and transform it into an executable artifact, while also downloading dependencies, resolving conflicts, and optimizing the compilation.

## Why do we use Build Systems?
- **Dependency Resolution**: If your code uses external libraries, the build system automatically downloads the correct versions.
- **Incremental Compilation**: In huge projects, recompiling everything from scratch would take hours. Build systems keep track of modified files and recompile *only* what is strictly necessary.
- **Automation**: They prevent developers from having to manually run dozens of tedious terminal commands in sequence.

---

## Examples by Ecosystem

Each programming language has developed its own standard tools.

### 1. C and C++: `Make` and `CMake`
The C/C++ world is historically the most complex.
- **Make**: Uses a file called `Makefile` containing rules to compile `.c` files into object files (`.o`) and then link them into an executable. It is very powerful but hard to maintain for cross-platform projects (Windows vs Linux).
- **CMake**: Is actually a **Meta-Build System**. You don't write direct compilation commands, but you write a `CMakeLists.txt` file that describes the project at a high level. CMake then *generates* Makefiles for Linux, or Visual Studio projects for Windows automatically.

### 2. JVM Ecosystem (Java, Scala): `Maven`, `Gradle`, `SBT`
These languages are compiled into *bytecode* that runs on the Java Virtual Machine.
- **Maven**: Uses an XML file (`pom.xml`). Very rigid but universal.
- **Gradle**: Uses scripts based on Groovy or Kotlin (`build.gradle`). Very flexible and the de facto standard for Android development.
- **SBT (Scala Build Tool)**: The standard for the Scala language. It is known for supporting interactive and continuous compilation.

### 3. Formal / Theoretical Languages (Lean 4): `Lake`
Lean 4 is a programming language and an interactive theorem prover.
- **Lake (Lean Make)**: Is the official package manager and build system for Lean 4. Since Lean is often used to mathematically verify libraries, Lake takes care of compiling `.lean` files while efficiently managing the complex hierarchy of mathematical imports.

### 4. Modern Languages (Rust, Go): `Cargo` and `Go Modules`
Modern languages are born with the build system directly integrated into the standard toolchain.
- **Cargo (Rust)**: You define the project in a `Cargo.toml`. Cargo downloads dependencies (Crates), compiles the code, and even runs tests (`cargo test`).
- **Go**: Natively uses `go build` and `go mod` to manage dependencies without having to download external tools.

### 5. Python and JavaScript: Interpreted Languages
Even though they are not "compiled" in the strict sense into machine code (Python is interpreted, JS is interpreted/JIT compiled), they still need toolchains.
- **JS/TS**: Use `npm`, `yarn`, or `pnpm` to install dependencies from a `package.json`, and tools like `Webpack` or `Vite` to minify and "compile" (transpile) Typescript into pure Javascript.
- **Python**: Uses files like `requirements.txt` or `pyproject.toml` via tools like `pip`, `poetry`, or `uv` to resolve and isolate dependencies.
