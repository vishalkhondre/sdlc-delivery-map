# Release lesson set

The seven lessons are in content/09-deep-release.json, in inventory order. The authors covered publication and change authority, deployment and rollout, and recovery and data compatibility in separate passes. Every lesson opens with a business question in plain language and includes an illustrative setting, a visible result, a failed example, and transfer guidance.

The records distinguish the Release Manager’s responsibility from the missing individual approval log. The operator verifies the named revision before testing effective application behavior. The Service Owner makes the pilot expansion decision after observation. Release notes use the verified audience and a private support path. The data migration and feature-flag setup are proposed designs. Neither is reported as a historic part of INC-7.

The deploy excerpts were exercised with simulated Azure CLI responses and real Bash and jq. The migration comparison was exercised with synthetic rows in a local SQL rehearsal. Those checks do not deploy a workload or establish PostgreSQL production performance or locking behavior.
