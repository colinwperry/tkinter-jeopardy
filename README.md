# Timer Implementation CHANGELOG

> **Disclaimer:** AI was not used in any part of this implementation process. If anything appears plagiarized, please clarify through contacting me.

---

## Commit Log
> Descending Order
* **chore:** remove unnecessary comments
  * Removed 14 lines of comments not vital to code comprehension

* **refactor:** modified reused variable declarations
  * Removed hardcoded reused variabes and sourced them to class-wide const vars

* **refactor:** modified unclear button state handling
  * Changed unclear button state handling from using 0 and 1 to a more clear boolean approach

* **feat:** implemented timer logic and widget handling
  * Imported the time library
  * Added the `is_complex` parameter to each `image_sets` dict
  * Added a new frame to hold the `timer_label`
  * Added a `complex` var to `button_info` detailing the button type from `image_sets`
  * Utilized button state handling to recognize when the timer needs to run
  * Implemented a function for timer decrementation

* **refactor:** added comprehensive type inference across arrays
  * Added type inference across any arrays and variables for future clarity

* **fix:** addressed bug where timer restarts after button reverts from answer->question
  * Implemented logic that ensures the timer doesn't restart when the button goes from the answer state back to the question state

* **fix:** addressed variable misname that broke timer logic
  * Fixed a minor bug involving the misnamed `timer_label` variable being just `"label"` inside the `increment_timer` function

* **style:** minor auto formatting

* **refactor:** rename increment_timer function to more accurately depict function use
  * Renamed the `increment_timer()` function to `decrement_timer()` as this timer counts down, not up
