#!/usr/bin/env bash
black --target-version=py314 cvbuilder && isort --profile=black cvbuilder
