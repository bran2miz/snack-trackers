# Django Models - Lab 27

## Author: Brandon Mizutani

Version: 1.0.0 (PR URL: [PR URL])

## Overview

This lab assignment required us to build out a project with one model and wire up that model using Django Views.

## Getting Started

### Lab 27

We had to create a project that followed the same steps as the previous lab, only this time we had to create a Snack model. The snack model includes:
-a name as a CharField with maximum length of 64 characters.
-a purchaser ForeignKey related to Django’s built in user model with CASCADE delete option.
-a description TextField

We had to also create a new class that included ListView and DetailView.

## Architecture

Python, Django, Models, get_user_model, superuser.

## Change Log

03-02-22 -- All tests are passing and the assignment is printing out the list of snacks that are saved in my admin user profile.

## Credit and Collaborations

Eddie Ponce

Alex Payne

Connor Boyce

Roger Huba