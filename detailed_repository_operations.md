# 仓库文件操作详解

本文档详细说明了我可以对仓库中的文件执行的各种操作，并提供了示例。

## 1. 修改文件内容 (Modifying Files)

我可以修改现有文件的内容。

**如何指示我：**
告诉我要修改哪个文件的哪部分内容，以及新的内容是什么。

**示例：**
假设有一个 `README.md` 文件，内容如下：
```markdown
# 项目标题
这是一个旧的项目描述。
```
您可以这样告诉我：“请修改 `README.md` 文件，将第二行‘这是一个旧的项目描述。’更改为‘这是一个更新后的项目描述。’”

**我将执行的操作（内部）：**
1. 读取 `README.md`。
2. 定位到第二行。
3. 将其替换为新内容。
4. 保存文件。

## 2. 重命名文件或目录 (Renaming Files/Directories)

我可以更改文件或目录的名称。

**如何指示我：**
提供旧的名称和新的名称，以及它是一个文件还是目录。

**示例：**
*   “请将文件 `old_name.txt` 重命名为 `new_name.txt`。”
*   “请将目录 `src/old_utils` 重命名为 `src/new_utils`。”

**我将执行的操作（内部）：**
使用类似 `git mv old_name.txt new_name.txt` 的命令。

## 3. 移动文件或目录 (Moving Files/Directories)

我可以将文件或目录从一个位置移动到另一个位置。

**如何指示我：**
提供文件/目录的当前路径和目标路径。

**示例：**
*   “请将文件 `config.txt` 从根目录移动到 `src/config/` 目录下。” (目标是目录)
*   “请将文件 `src/old_path/image.png` 移动到 `assets/images/image.png`。” (目标是完整路径)

**我将执行的操作（内部）：**
使用类似 `git mv config.txt src/config/` 或 `git mv src/old_path/image.png assets/images/image.png` 的命令。

## 4. 创建新目录 (Creating Directories)

我可以创建新的目录（文件夹）来组织文件。

**如何指示我：**
告诉我要创建的目录的路径。

**示例：**
“请在 `src/` 目录下创建一个名为 `components` 的新目录。”

**我将执行的操作（内部）：**
使用类似 `mkdir -p src/components` 的命令。为了让 Git 跟踪这个空目录（如果需要），通常会创建一个 `.gitkeep` 文件在里面，然后 `git add src/components/.gitkeep`。

## 5. 合并分支 (Merging Branches)

如果您有不同的分支，我可以将一个分支的更改合并到另一个分支。

**如何指示我：**
告诉我要合并的源分支和目标分支。

**示例：**
“请将 `feature/new-login` 分支合并到 `develop` 分支。”

**我将执行的操作（内部）：**
1. `git checkout develop`
2. `git merge feature/new-login`

## 6. 解决合并冲突 (Resolving Merge Conflicts)

在合并分支时，如果出现冲突，我需要您的明确指示来解决。

**如何指示我：**
当冲突发生时，我会向您展示冲突的文件和具体内容。您需要告诉我：
*   对于每个冲突的部分，是保留当前分支的版本、传入分支的版本，还是两者都保留，或者是一个全新的版本。

**示例：**
假设合并时 `style.css` 文件冲突：
```
<<<<<<< HEAD (current branch: develop)
  color: blue;
=======
  color: red;
>>>>>>> feature/new-login (incoming branch)
```
您可以说：“在 `style.css` 的冲突中，保留 `develop` 分支的 `color: blue;`。”

**我将执行的操作（内部）：**
1. 手动编辑冲突文件，根据您的指示选择内容。
2. `git add style.css`
3. `git commit` (如果所有冲突都已解决)

## 7. 应用补丁 (Applying Patches)

如果您有 `.patch` 文件，我可以尝试将其应用到仓库中。

**如何指示我：**
提供 `.patch` 文件的路径或内容。

**示例：**
“请应用位于 `patches/fix_bug_123.patch` 的补丁文件。”

**我将执行的操作（内部）：**
使用类似 `git apply patches/fix_bug_123.patch` 的命令。

## 8. 恢复旧版本 (Reverting/Checking Out)

我可以将文件或整个仓库恢复到之前的某个提交状态。

**如何指示我：**
*   **恢复单个文件到特定提交：** “请将 `src/main.js` 文件恢复到提交 `abcdef1` 时的状态。”
*   **检出整个仓库到特定提交（分离头指针状态）：** “请检出提交 `abcdef1`。” (注意：这会使仓库处于分离头指针状态，后续提交不会在任何分支上，除非创建新分支。)
*   **撤销某个提交的更改 (创建一个新的反向提交)：** “请撤销提交 `abcdef1` 的更改。”

**我将执行的操作（内部）：**
*   恢复单个文件: `git checkout abcdef1 -- src/main.js`
*   检出整个仓库: `git checkout abcdef1`
*   撤销提交: `git revert abcdef1`

## 9. 标签操作 (Tagging)

我可以为特定的提交创建、列出或删除标签（例如，版本号）。

**如何指示我：**
*   **创建标签：** “请为当前 `HEAD` 创建一个轻量标签 `v1.0.0`。” 或 “请为提交 `abcdef1` 创建一个带附注的标签 `v1.0.1-beta`，附注信息是‘第一个beta版本’。”
*   **列出标签：** “请列出所有的标签。”
*   **删除标签：** “请删除标签 `v0.9-alpha`。” (注意：删除本地标签后，如果已推送到远程，远程标签通常需要单独删除。)

**我将执行的操作（内部）：**
*   创建轻量标签: `git tag v1.0.0`
*   创建带附注标签: `git tag -a v1.0.1-beta -m "第一个beta版本" abcdef1`
*   列出标签: `git tag`
*   删除标签: `git tag -d v0.9-alpha`

## 10. 执行脚本和命令 (Running Scripts/Commands)

我可以执行仓库中包含的脚本或任意的 shell 命令。

**如何指示我：**
明确告诉我要执行的命令或脚本路径及其参数。

**示例：**
*   “请运行 `./scripts/build.sh` 脚本。”
*   “请执行 `npm install` 命令来安装依赖。”
*   “请运行 `python tests/run_all_tests.py --verbose`。”

**我将执行的操作（内部）：**
直接在 shell 中执行您提供的命令。

## 通用提交流程

对于上述大多数会修改工作区或暂存区的操作，我通常会遵循以下步骤将更改持久化：

1.  **执行操作：** 例如修改文件、移动文件、删除文件等。
2.  **添加到暂存区 (Staging)：** 使用 `git add <file_path>` 或 `git add .` (如果适用)。
3.  **提交到指定分支 (Committing)：**
    *   切换到目标分支 (例如 `git checkout main`)。
    *   提交更改，并使用您提供的提交信息 (例如 `git commit -m "feat: 更新项目描述"`).
    *   如果需要创建新分支，我会先 `git checkout -b <new_branch_name>`。

如果您没有指定分支或提交信息，我会向您确认或使用一个通用的描述。

---

希望这些详细的说明和示例能帮助您更好地指导我完成仓库操作！
