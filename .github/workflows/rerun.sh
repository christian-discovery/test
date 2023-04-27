- name: Trigger workflow
  run: |
    for i in {1..3}; do
      curl -X POST \
        -H "Accept: application/vnd.github.v3+json" \
        -H "Authorization: token ${{ secrets.PAT }}" \
        https://api.github.com/repos/${{ test }}/actions/workflows/${{ Trial }}/dispatches \
        -d '{"ref":"${{ github.ref }}"}'
      sleep 30
    done
