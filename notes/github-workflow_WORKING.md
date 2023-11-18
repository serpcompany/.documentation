# Github Collaboration Workflow

## Branches Overview

### Branch 1: Main/Production

- Stable code that is deployed.
- Restricted direct commits and merges from the development/integration branch after testing. Enforceable through GitHub branch protection rules.


### Branch 2: Development/Integration

- Serves as a staging area for features and bug fixes. It's a copy of the main/production branch but for integration purposes.
- Can be used to build staging website & run less-frequent/longer-running tests, etc.  
- This branch is where much of the longer-running automated testing happens before code is deemed ready for production.


### Branch 3+: Feature Branches

1. For every "task/issue" developers should create a feature branch. 
2. Feature branches are created by branching off of the development/integration branch  (should never interact directly with the main/production branch).
3. Feature branches should be worked on locally (write tests, write code, make commits, etc.) h 
4. When the feature is complete on local it should be pushed into the remote branch, which should trigger a pull request which kicks off automated additional tests, automated code reviews, etc.


---

## Workflow Overview

### 1. Create a branch to work on a new feature or bug fix.

- Create a feature branch off of the development branch (following our branch naming conventions)
- Navigate to the issue in your GitHub repository.
- Use the "Create a branch for this issue" feature.
- Select development as the base branch from which your new feature branch will diverge.

### 2. Update Your Local development Branch:
```
git checkout development
git fetch origin development
git merge origin/development
git switch -c <new-branch-name>
```

### 3. Code:

- Write tests & code locally (following TDD). 
- Make sure you update/sync your branch with what (may have) changed on the remote by running (at least once per day, or anytime you see a notification that another developers changes/code/push has been merged into the development branch):

```
git fetch origin development
git merge origin/development
```

- When the feature is complete on local and all tests are run & pass, you can push to the remote branch.
- Stage your changes: When ready, stage changes & commit. This kicks off the automated CI process. 

```
git add path/to/file1 path/to/file2
git commit -m "A message following our commit message conventions"
```

- After committing your changes locally, make sure your stuff is current to the remove, then push to the remote feature branch.
  
```
git fetch origin development
git merge origin/development
git push origin/<new-branch-name>
```



### CICD Phase 1: Level 1 tests (Unit Tests & Code Quality)

- CICD automations run all unit tests (never assume the developer ran them).
- CICD automations run inspections on Code Quality/Standards/etc.

If anything **FAILS**: 

- Testing stops. 
- A report is generated & notifications are sent. 
- The CI process halts. Immediate fixes are expected by developer. 
- When the fix is complete on local and all tests are run & pass, developer can push to the remote branch.

If all **PASS**:
  
- A report is generated & notifications are sent.
- Developer fetches any changes/updates from the `development` branch to merge into the feature branch, then creates a pull request to the `development` branch.


### CICD Phase 2: Level 2 tests (Functional/System Tests + GUI Tests & Performance Audits)

- CICD automations build environment to support any "Functional/System Tests" involving database and other external dependencies & runs tests.
- CICD automations build environment to support any additional GUI Tests & Performance Audits (like Selenium, Lighthouse, etc.) & runs tests.

If anything **FAILS**: 

- Testing stops 
- A report is generated & notifications are sent. 
- The pull request is rejected. 
- The CI process halts. Immediate fixes are expected by developer. 
- When the fix is complete, the pull request can be initiated again.

If all **PASS**:

- Build is committed, merged & tagged.
- The CI process continues.


### CICD Phase 3: Deployment

- `development` branch is merged into `main/production` branch. 
- CICD automations deploy the build to the production environment.
- Build/release is tagged.
- Report is generated and a notification is sent.

### CICD Phase 4: Clean-up

- Feature branch is deleted.
