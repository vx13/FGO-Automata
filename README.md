# FGO-Automata

![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/Meowcolm024/FGO-Automata?include_prereleases)
![GitHub issues](https://img.shields.io/github/issues/Meowcolm024/FGO-Automata)
![GitHub](https://img.shields.io/github/license/meowcolm024/FGO-Automata)

**FGO-Automata** allows you to play FGO just like writting *Python* Script

**注意FGO-Automata适用于国服的Fate/Grand Order.** PS：[中文版README](README_CN.md)

## Install

Required libs: *ADB*, *PIL*, *OpenCV* and *numpy*

1. Install *ADB*(macOS): ```brew cask install android-platform-tools```
2. Install *PIL*, *OpenCV* and *numpy*: ```pip install opencv-python numpy pillow```
3. Clone the repo: ```git clone https://github.com/Meowcolm024/FGO-Automata.git```

## References

### 1. Initialization

#### a. Import package

```python
from core.Automata import Automata
```

* First import the package

#### b. Setup the Class

```python
shiki = Automata("assets/checkpoint.png", "assets/qp.png", (248, 0))
```

```python
ryougi = Automata("assets/checkpoint.png", "assets/qp.png")
```

* The first argument and the second one refers to the **path** of your **template** of checkpoint and **support servant**.
* And the third argument is also optional, if you screen resolution is *1920x1080*, just leave it blank or replace it with `(0,0)`.
* In the third argument, only add them if there are blues straps at the edges. For `(x, y)`, *x* refers to the shifts in x-axis shift, *y* refers to y-axis shift.

#### c. AP related (Optional)

```python
shiki.set_apples(0, "assets.silver.png")
```

* If you are using it as a automation bot, you may encounter AP problem which need to use *Gold Apples*.
* Notice that the function recieves 2 arguments. The first item is number, representing how many apples will be consumed. The second one refers to the **path** of your **template** of the type of the apple (incl. *Quartz*).

### 2. Start battle

```python
# start
shiki.select_checkpoint("assets/checkpoint2.png") # the argument is optional
shiki.select_support("assets/qp2.png") # the argument is optional
shiki.start_battle()
```

* You can choose other checkpoints and supports if needed
* If you don't need to modify your checkpoints and supports you can use:

```python
shiki.quick_start()
```

### 3. During battle

#### 1. Select cards

```python
shiki.select_cards([7])
```

```python
ryougi.select_cards([1,2,3])
```

* Notice this function receives a *list* of maximum **3** numbers. If the list is empty or has less numbers, more cards from normal cards will be selected randomly.
* For the numbers' meaning: Number **1~5** refer to the *normal cards* from **left** to **right**. Number **6,7,8** refer to *NP cards*.
* Cards will be taped in orders

#### 2. Select Servant skills

```python
# skill w/o target
shiki.select_servant_skill(4)
```

```python
# with target Servant
ryougi.select_servant_skill(2, 3)
```

* Notice this function receives a number.
* The number can be in the range of **1~9**, each refers to the skill counted from left.
* You can also add the second argument for the target *Servant*(See: [*Select Servants*](#4-select-servant-deprecated))

#### 3. Select Master skills

```python
# skill w/o target
shiki.select_master_skill(2)
```

```python
# with target Servant
ryougi.select_master_skill(1, 3)
```

```python
# Order Change
rin.select_master_skill(3, 1, 1)
```

* Notice this function receives a number.
* The number can be in the range of **1~3**, each refers to the skill counted from left.
* You can also add the second argument for target *Servant*(See: [*Select Servants*](#4-select-servant-deprecated))
* If the skill is *Order Change*, you can add the third argument(See: [*Change Servants*](#5-change-servants-deprecated))

#### 4. Select Servant (DEPRECATED)

```python
shiki.select_servant(1)
```

* **NOTICE: This function has been integrated to `select_servant_skill` and `select_master_skill`, so you don't need to use it explicitly. (Besides, the reference below is still vaild.)**
* There are some skills in *FGO* have target servant, if the skill you have chosen is this kind of skill, you may need to use this function to choose the desired *Servant*.
* Notice this function receives a number.
* The number can be in the range of **1~3**, each refers to the *Servant* counted from left.

#### 5. Change Servants (DEPRECATED)

```python
shiki.change_servant(1, 1)
```

* **NOTICE: This function has been integrated to `select_master_skill`, so you don't need to use it explicitly. (Besides, the reference below is still vaild.)**
* This function receives 2 numbers, each should be in the range of **1~3**.
* The first arg refers to the first 3 Servants and the second one refers to the last 3.

### 4. Finish battle

```python
# finish
shiki.finish_battle()
```

### 5. Other functions

#### 1. Wait for a certain scene

```python
shiki.wait("assets/checkpoint.png")
```

* It allows you idle the script till a certain scene
* It receives an argument of the *path* of the template image.

#### 2. Tap screen

```python
shiki.tap((100, 100), 0, 0)
```

* Allows to tap a certain point in the screen
* The first arg is a tuple of the coordinate `(x, y)`
* The 2nd and the 3rd args are random shifts in x and y, if you don't want have any shifts, replace with `0`

#### 3. Toggle Master Skill

```python
shiki.toggle_master_skill()
```

* You can use this function to turn on/off the _Master_ skill panel.

## TO-DO

* Advance support
