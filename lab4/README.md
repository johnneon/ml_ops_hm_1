# MLOps: Task №3

This lab is example of working with data version control - [dvc](https://dvc.org/).

## Main

We had to make some steps:
1. Prepare dataset
2. Start tracking it with dvc
3. Change dataset and save results with git+dvc
4. One more step above
5. Try to back to first dataset version
6. Try to back to second dataset version
7. Try to back to final dataset version

As remote storage chosen [Google Drive folder](https://drive.google.com/drive/folders/1lHf_W9A27S8t_YUCJXdNOruY7gBPbxWV?usp=drive_link).

So, we need to see our get commits with `git log --oneline`:

```shell
fe4a014 feat: add base structure of lab4
f158ffc feat: init dvc
26b29e6 feat: stop tracking lab4/datasets
d8d20cb feat: start tracking datasets with dvc
6ccd527 feat: add remote storage
a7dddcf feat: update dataset with first prep
b73f4a7 feat: update dataset with second prep
31d45bb fix: fix second prep and rerun it
```

We can see there are needle commits - `d8d20cb`, `a7dddcf`, `31d45bb`

To get results for 5,6,7 steps of our plan we need to check out
to our commits one by one with `git checkout <commit-id>`, and then
run `dvc pull`, so we can get our dataset versions to see them.

And finally, to get back to last dataset we should run:
```shell
git checkout master
dvc pull
```

## A bit about application

`model.py` - download data and save it to datasets folder
`first_prep.py` - modifying dataset with StandardScaler
`second_prep.py` - modifying dataset with PowerTransformer

To run all those scripts - be sure you are currently in `lab4` dir.

As for dvc, I had to init it in root of project because if git,
if you try to run `dvc init` in other folder (without git), you will get
the following error:
```
ERROR: failed to initiate DVC - /Users/johnneon/MachineLearning/ml_ops_hm_1/lab4 is not tracked by any supported SCM tool (e.g. Git). Use `--no-scm` if you dont want to use any SCM or `--subdir` if initializing inside a subdirectory of a parent SCM repository.
```