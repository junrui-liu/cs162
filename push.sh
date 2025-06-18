#!/bin/bash

mdbook build
scp -r book csil:/cs/student/junrui/public_html/cs162
