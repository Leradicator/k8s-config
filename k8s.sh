set +e
    eksctl --verbose 5 create cluster --with-oidc --without-nodegroup --kubeconfig ~/.kube/config --auto-kubeconfig -v 5 -f cluster.yaml
    echo "CREATE EXITED with: $?"
set -e

set +e
    eksctl --verbose 5 create nodegroup -f bootstrap-command.yaml
    echo "CREATE EXITED with: $?"
set -e
