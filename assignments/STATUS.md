# STATUS.md — Cloudmesh-AI / DevOps Class Progress

## Missed Class / Attendance

- **November 29, 2026:** Missing class; professor notified via email.
- I have been making an effort to attend lectures regularly. When I have joined late, I have followed up using the lecture recordings.
- I have not been keeping up with every Piazza post and follow-up. I am reviewing missed updates, identifying outstanding work, and using this file to track my progress.

## Class Catch-Up and Piazza

- [x] Review unread Piazza posts and follow-up discussions.
- [x] Configure Piazza to notify me of both new posts and replies.
- [x] Check the [weekly assignment page](https://cloudmesh-ai.github.io/cloudmesh-ai-lecture/lecture/assignments/assignments/) for missed or updated requirements.
- [x] Create `STATUS.md` to track outstanding tasks and weekly progress.
- [ ] Continue updating `STATUS.md` as assignments are completed.

## Development Environment, GitHub, and Bash

- [ ] Keep all class-related repositories in one directory (for example, `~/work`).
- [x] Verify GitHub SSH key authentication and practice cloning repositories using SSH.
- [x] Review Bash / Git Bash commands and be prepared to demonstrate them.
- [x] Launch VS Code from a Bash terminal with `code .`; document any issues and fixes.
- [ ] Record a short demonstration of Git Bash, GitHub SSH keys, and LLM usage in Cline, if not already submitted.
- [ ] Read the `cloudmesh-ai-vm` `README.md`, including Basic Usage, VM Doctor, and Troubleshooting.
- [ ] Read `CONTRIBUTING.md`, especially the Code Formatting section.

## November 12 Assignments — Review / Completion Pending

- [ ] **Assignment 1:** Finish the class catch-up, Piazza, Bash, GitHub, VS Code, and related tasks.
- [ ] **Assignment 2:** Work on [cloudmesh-ai-vm issue #116](https://github.com/cloudmesh-ai/cloudmesh-ai-vm/issues/116) or improve the WSL2 VM implementation.
- [ ] **Assignment 3:** Prepare a Git Bash, GitHub SSH key, and repository organization demonstration.
- [x] Set up and verify access to the Jetstream LLM.
- [ ] Review the three sample academic project reports shown in class.

## cloudmesh-ai-vm — Weekly Contributions

- [ ] Work each week on the three selected VM providers.
- [ ] Use the `dev3` branch as instructed.
- [ ] Run existing smoke tests and add tests as needed.
- [x] Review the codebase with an LLM and prepare an improvement plan.
- [ ] Check existing issues and pull requests before filing new issues.
- [ ] Implement and verify small, meaningful improvements.
- [ ] Submit pull requests when appropriate and permitted by the assignment; coordinate on overlapping work.
- [ ] Review related student pull requests.
- [ ] Document completed work, test results, issues, and pull request URLs in this file.
- [ ] Check LLM-generated changes manually for hallucinations, regressions, or accidental deletions.

### Contributions / Pull Requests

- **Progress:** To be updated.
- **Issues:** To be added.
- **Pull requests:** To be added.
- **Smoke-test results:** To be added.

## Chameleon and Configuration Testing

- [ ] Review and run the Chameleon standalone test (`tests/standalone/gregor-kvm-tacc-lease-chi.py`).
- [x] Review the current `python-chi` source code and its differences from published documentation.
- [ ] Check whether authentication requires sourcing `openrc.sh` instead of relying on `~/.config/openstack/clouds.yaml` for the relevant test.
- [ ] Run `test_config.py` and report any issues.
- [ ] Review VM Doctor improvements, including `--cloud=all` and authentication validation.

## Project — E-commerce Application with Containerized RAG and Local AI Inference

### Current Progress

- **Prebuilt e-commerce application:** **PrestaShop**.
- **Local setup:** PrestaShop has been tested in a local Docker environment with its MySQL database.
- **Cloud deployment:** The application has **not yet been tested in a cloud environment**.
- **RAG pipeline:** The remaining RAG components and their integration are **still under development**.

### Project Tasks

- [x] Select PrestaShop as the prebuilt e-commerce application.
- [x] Test PrestaShop locally using Docker and MySQL.
- [ ] Deploy and test the e-commerce application in a cloud environment.
- [ ] Continue building and integrating the RAG pipeline, including retrieval, vector storage, and local AI inference.
- [ ] Work on the frontend and connect it to the required application services.
- [ ] Update `project.md` as an intermediate academic project report, rather than labeling it a proposal.
- [ ] Document the architecture, implementation, tests, and results.
- [ ] Add an acknowledgement section explaining how LLMs were used and to what extent.
- [ ] Create `docs/README.md` with setup and run instructions and integrate it into MkDocs.
- [ ] Prepare screenshots or a short demonstration video as appropriate.
- [ ] Provide a short project progress update each week.

## Additional Review / Self-Study

- [ ] Review the optional [AWS emulator chapter](https://cloudmesh-ai.github.io/cloudmesh-ai-lecture/section/cloud/vm-cloud/aws-emulator-chapter/).
- [ ] Report documentation issues or improvements through the appropriate repository workflow.
- [ ] Ask questions on Piazza when requirements or technical issues are unclear.

## Next Steps

- Continue working on the project, with the goal of **starting frontend development by Thanksgiving week**.
  - Use an LLM to help plan the frontend and create an initial draft over the weekend, ideally before Thanksgiving; review and validate the output rather than relying on generated code without checking it.
- Continue contributing to the `cloudmesh-ai-vm` project and regularly updating `STATUS.md` with completed tasks, tests, issues, pull requests, and outstanding work.
