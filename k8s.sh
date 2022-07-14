#export AWS_ACCESS_KEY_ID=AKIAV6YLOSY54PAB2VOZ
#export AWS_SECRET_ACCESS_KEY=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

set +e
    eksctl --verbose 5 create cluster --with-oidc --without-nodegroup --kubeconfig ~/.kube/config --auto-kubeconfig -v 5 -f cluster.yaml
    echo "CREATE EXITED with: $?"
set -e

set +e
    eksctl --verbose 5 create nodegroup -f bootstrap-command.yaml
    echo "CREATE EXITED with: $?"
set -e

## needs update of publicAccess and privateAccess once eksctl create done
#eksctl utils update-cluster-endpoints -f bootstrap-command.yaml --approve
