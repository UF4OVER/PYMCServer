
## 命名规范
### 命名法
* 变量名采用 snake_case。
* 方法名沿袭 PyQt 特点，采用 lowerCamelCase
* 类名采用 UpperCamelCase
* 旗标类、枚举类和常量采用全大写命名

### 命名构成
#### 变量名
* 采用正常英文语序命名，例如 `day_counter`, `month_counter`, `year_counter`
* 具有大量语义类似，而类型不同的变量，将强调的类型提前作为前缀，例如 `container_name`, `label_name`
* 变量名与方法名冲突时，变量名后加 `_` 后缀，如 `self.name()`, `self.name_`


## 控件 / 组件类
约定模版化的方法和其功能。
### MCS+Module+page
作为每个界面主类的命名规范
