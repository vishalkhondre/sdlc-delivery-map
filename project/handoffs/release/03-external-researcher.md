# Release source register

Opened 21 November 2026. The Release authors checked the references while drafting. The table identifies the lesson using each source. Jira versions, Git references, SemVer and GitHub release notes establish what each publication record can say. The change types and GitHub environment guides describe possible mechanisms. The example assigns authority under a fictional standard-change policy.

For the deployment sample, the Azure Login v2.3.0 release supplies the pinned action. GitHub documents job permissions and environment protection. Azure documents revision creation and naming, scale and health fields, traffic selection and the CLI inspection commands. The revision template shows the selected configuration reference. Application observations establish effective routing. The handoff and tests deliberately stop short of claiming a live deployment.

The recovery and data examples draw on the Azure and Google operations guides, AWS compatibility guidance, and PostgreSQL semantics for adding columns and comparing values with nulls. The sample migration is a rehearsal for mixed-version readers and writers. The qualification-record download supplies the two production attempts and their measured outcomes.

| Primary source and URL | Release lessons |
|---|---|
| [Atlassian Support · Manage versions](https://support.atlassian.com/jira-cloud-administration/docs/manage-versions/) | versioning-and-fix-version, release-notes-practice |
| [Pro Git · Git Basics — Tagging](https://git-scm.com/book/en/v2/Git-Basics-Tagging) | versioning-and-fix-version |
| [Git · git-rev-parse](https://git-scm.com/docs/git-rev-parse) | versioning-and-fix-version |
| [GitHub Docs · About releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) | versioning-and-fix-version, release-notes-practice |
| [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html) | versioning-and-fix-version |
| [GitHub Docs · Deployments and environments](https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments) | change-approval, deploy-workflow-anatomy |
| [Microsoft Learn · Architecture strategies for safe deployment practices](https://learn.microsoft.com/en-us/azure/well-architected/operational-excellence/safe-deployments) | change-approval, rollback-rollforward |
| [Atlassian · Change management types](https://www.atlassian.com/itsm/change-management/types) | change-approval |
| [GitHub Docs · Configuring OpenID Connect in Azure](https://docs.github.com/en/actions/how-tos/secure-your-work/security-harden-deployments/oidc-in-azure) | deploy-workflow-anatomy |
| [GitHub Docs · Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax) | deploy-workflow-anatomy |
| [Azure Login Action v2.3.0](https://github.com/Azure/login/releases/tag/v2.3.0) | deploy-workflow-anatomy |
| [Microsoft Learn · Update and deploy changes in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/revisions) | deploy-workflow-anatomy, rollout-strategies, rollback-rollforward |
| [Microsoft Learn · Traffic splitting in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/traffic-splitting) | deploy-workflow-anatomy, rollout-strategies |
| [Microsoft Learn · az containerapp](https://learn.microsoft.com/en-us/cli/azure/containerapp?view=azure-cli-latest) | deploy-workflow-anatomy |
| [Microsoft Learn · az containerapp revision](https://learn.microsoft.com/en-us/cli/azure/containerapp/revision?view=azure-cli-latest) | deploy-workflow-anatomy |
| [Microsoft Learn · Health probes in Azure Container Apps](https://learn.microsoft.com/en-us/azure/container-apps/health-probes) | deploy-workflow-anatomy |
| [Microsoft Learn · Container Apps Revisions - List Revisions](https://learn.microsoft.com/en-us/rest/api/resource-manager/containerapps/container-apps-revisions/list-revisions?view=rest-resource-manager-containerapps-2026-07-01) | deploy-workflow-anatomy |
| [Azure · Container Apps Deploy Action](https://github.com/Azure/container-apps-deploy-action) | deploy-workflow-anatomy |
| [jq 1.7 Manual](https://jqlang.org/manual/v1.7/) | deploy-workflow-anatomy |
| [Microsoft Learn · Understand feature management using Azure App Configuration](https://learn.microsoft.com/en-us/azure/azure-app-configuration/concept-feature-management) | rollout-strategies |
| [Google SRE Workbook · Canarying Releases](https://sre.google/workbook/canarying-releases/) | rollout-strategies |
| [Google SRE Workbook · Incident Response](https://sre.google/workbook/incident-response/) | rollback-rollforward |
| [AWS Builders’ Library · Ensuring rollback safety during deployments](https://aws.amazon.com/builders-library/ensuring-rollback-safety-during-deployments/) | rollback-rollforward, data-change-coordination |
| [PostgreSQL · 5.8. Modifying Tables](https://www.postgresql.org/docs/current/ddl-alter.html) | data-change-coordination |
| [PostgreSQL · ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html) | data-change-coordination |
| [PostgreSQL · 9.2. Comparison Functions and Operators](https://www.postgresql.org/docs/current/functions-comparison.html) | data-change-coordination |
| [GitHub Docs · Automatically generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes) | release-notes-practice |
