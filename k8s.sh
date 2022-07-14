set +e
    eksctl --verbose 5 create cluster --with-oidc --without-nodegroup --kubeconfig ~/.kube/config --auto-kubeconfig -v 5 -f cluster.yaml
    echo "CREATE EXITED with: $?"
set -e

eksctl create addon --name kube-proxy --cluster k8s-eks-in-this-vpc --force

set +e
    eksctl --verbose 5 create nodegroup -f bootstrap-command-control-plane.yaml --cfn-disable-rollback
    echo "CREATE EXITED with: $?"
set -e

set +e
    eksctl --verbose 5 create nodegroup -f bootstrap-command-worker.yaml --cfn-disable-rollback
    echo "CREATE EXITED with: $?"
set -e
