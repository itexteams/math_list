import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang31_p2_b1_c2_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Random các thông số cho bài toán
            choices = [
                (10, 20, 500),
                (10, 15, 300),
                (15, 20, 600),
                (15, 25, 750),
                (20, 25, 1000),
                (10, 25, 500),
                (10, 30, 600)
            ]
            in_x, in_y, V = random.choice(choices)
            p_x = random.randint(2, 5)
            p_y = random.randint(5, 12)
            out_x = in_x + p_x
            out_y = in_y + p_y

            max_x = V // in_x
            max_y = V // in_y

            # Nội dung câu hỏi
            noidungcauhoi = ('''Bạn An dự định kinh doanh online hai mặt hàng là móc khóa và sổ tay với số vốn không vượt quá $%s$ nghìn đồng. Một móc khóa bạn nhập về $%s$ nghìn đồng và bán ra $%s$ nghìn đồng, một quyển sổ tay bạn nhập về $%s$ nghìn đồng và bán ra $%s$ nghìn đồng. Gọi $x, y$ lần lượt là số móc khóa, số sổ tay mà bạn nhập về. Giả sử số hàng nhập về đều được bán hết và chưa tính các lần quay vòng vốn tiếp theo.'''                  
                             % (V, in_x, out_x, in_y, out_y))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Các bất phương trình bậc nhất thể hiện số móc khóa An có thể nhập về là $0 \\le x \\le %s$' % max_x
            nb_da_1_s = 'Các bất phương trình bậc nhất thể hiện số móc khóa An có thể nhập về là $0 \\le x \\le %s$' % (max_x + random.randint(5, 10))

            loigiai_nb_d = ('''Gọi $x$ là số móc khóa, ta có $x \\ge 0, x \\in \\mathbb{N}$. \\\\
            Số vốn tối đa là $%s$ nghìn đồng, nhập mỗi móc khóa $%s$ nghìn đồng. \\\\
            Khi đó số tiền nhập móc khóa không vượt quá số vốn nên: $%sx \\le %s \\Leftrightarrow x \\le %s$. \\\\
            Vậy $0 \\le x \\le %s$. \\\\
            Mệnh đề đúng.''' % (V, in_x, in_x, V, max_x, max_x))

            loigiai_nb_s = ('''Gọi $x$ là số móc khóa, ta có $x \\ge 0, x \\in \\mathbb{N}$. \\\\
            Số vốn tối đa là $%s$ nghìn đồng, nhập mỗi móc khóa $%s$ nghìn đồng. \\\\
            Khi đó số tiền nhập móc khóa không vượt quá số vốn nên: $%sx \\le %s \\Leftrightarrow x \\le %s$. \\\\
            Vậy $0 \\le x \\le %s$. \\\\
            Mệnh đề sai.''' % (V, in_x, in_x, V, max_x, max_x))

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Các bất phương trình bậc nhất thể hiện số quyển sổ tay An có thể nhập về là $0 \\le y \\le %s$' % max_y
            th_da_1_s = 'Các bất phương trình bậc nhất thể hiện số quyển sổ tay An có thể nhập về là $y > %s$' % max_y

            loigiai_th_d = ('''Gọi $y$ là số quyển sổ tay, ta có $y \\ge 0, y \\in \\mathbb{N}$. \\\\
            Khi đó số tiền nhập sổ tay không vượt quá số vốn nên: $%sy \\le %s \\Leftrightarrow y \\le %s$. \\\\
            Vậy $0 \\le y \\le %s$. \\\\
            Mệnh đề đúng.''' % (in_y, V, max_y, max_y))

            loigiai_th_s = ('''Gọi $y$ là số quyển sổ tay, ta có $y \\ge 0, y \\in \\mathbb{N}$. \\\\
            Khi đó số tiền nhập sổ tay không vượt quá số vốn nên: $%sy \\le %s \\Leftrightarrow y \\le %s$. \\\\
            Mệnh đề sai.''' % (in_y, V, max_y))

            ######################################################################## Vận dụng ############################################
            # Tạo dữ liệu ngẫu nhiên
            x_c_true = random.randint(1, max_x // 2)
            y_c_true = random.randint(1, (V - in_x * x_c_true) // in_y)
            cost_true = in_x * x_c_true + in_y * y_c_true

            x_c_false = random.randint(max_x // 2 + 1, max_x - 1)
            y_c_false = ((V - in_x * x_c_false) // in_y) + random.randint(2, 5)
            cost_false = in_x * x_c_false + in_y * y_c_false

            # Các đáp án
            vd_da_1_d = '\\True Bạn An có thể nhập được $%s$ móc khóa và $%s$ quyển sổ tay' % (x_c_true, y_c_true)
            vd_da_1_s = 'Bạn An có thể nhập được $%s$ móc khóa và $%s$ quyển sổ tay' % (x_c_false, y_c_false)

            loigiai_vd_d = ('''Để nhập được $%s$ móc khóa và $%s$ quyển sổ tay thì số vốn cần có là: \\\\
            $%s \\cdot %s + %s \\cdot %s = %s$ (nghìn đồng). \\\\
            Vì $%s \\le %s$ nên An có thể nhập được. \\\\
            Mệnh đề đúng.''' % (x_c_true, y_c_true, in_x, x_c_true, in_y, y_c_true, cost_true, cost_true, V))

            loigiai_vd_s = ('''Để nhập được $%s$ móc khóa và $%s$ quyển sổ tay thì số vốn cần có là: \\\\
            $%s \\cdot %s + %s \\cdot %s = %s$ (nghìn đồng). \\\\
            Vì $%s > %s$ nên An không thể nhập được. \\\\
            Mệnh đề sai.''' % (x_c_false, y_c_false, in_x, x_c_false, in_y, y_c_false, cost_false, cost_false, V))

            ######################################################################## Vận dụng cao ############################################
            y_min = max_y - random.randint(1, 3)
            max_F = 0
            for y_val in range(y_min, max_y + 1):
                x_val = (V - in_y * y_val) // in_x
                F = p_x * x_val + p_y * y_val
                if F > max_F:
                    max_F = F
            F_max_true = max_F
            F_max_false = F_max_true + random.choice([-5, -2, 3, 5])

            # Các đáp án
            vdc_da_1_d = '\\True Khi bạn An nhập ít nhất $%s$ quyển sổ tay thì số tiền lãi nhiều nhất là $%s$ nghìn đồng' % (y_min, F_max_true)
            vdc_da_1_s = 'Khi bạn An nhập ít nhất $%s$ quyển sổ tay thì số tiền lãi nhiều nhất là $%s$ nghìn đồng' % (y_min, F_max_false)

            # Xây dựng chuỗi phân tích chi tiết cho Vận dụng cao
            y_range_str = "; ".join([str(i) for i in range(y_min, max_y + 1)])
            loigiai_vdc_d = ('''Số tiền lãi khi bán 1 móc khóa là $%s - %s = %s$ (nghìn đồng). \\\\
            Số tiền lãi khi bán 1 sổ tay là $%s - %s = %s$ (nghìn đồng). \\\\
            Lợi nhuận thu được là $F(x,y) = %sx + %sy$. \\\\
            Khi An nhập ít nhất $%s$ sổ tay, tức là $y \\ge %s$. Mà $y \\le %s$ nên $y \\in \\{%s\\}$. \\\\
            ''' % (out_x, in_x, p_x, out_y, in_y, p_y, p_x, p_y, y_min, y_min, max_y, y_range_str))

            for y_val in range(y_min, max_y + 1):
                x_val = (V - in_y * y_val) // in_x
                F = p_x * x_val + p_y * y_val
                loigiai_vdc_d += '''Với $y = %s \\Rightarrow x \\le \\lfloor \\frac{%s - %s \\cdot %s}{%s} \\rfloor = %s \\Rightarrow F = %s \\cdot %s + %s \\cdot %s = %s$. \\\\
            ''' % (y_val, V, in_y, y_val, in_x, x_val, p_x, x_val, p_y, y_val, F)

            loigiai_vdc_s = loigiai_vdc_d + '''Vậy số tiền lãi nhiều nhất là $%s$ nghìn đồng, không phải $%s$ nghìn đồng. \\\\ Mệnh đề sai.''' % (F_max_true, F_max_false)
            loigiai_vdc_d += '''Vậy số tiền lãi nhiều nhất là $%s$ nghìn đồng. \\\\ Mệnh đề đúng.''' % F_max_true


            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Gom nhóm phương án và lời giải để đồng bộ logic khi xáo trộn
            list_nb = [(nb_da_1_d, loigiai_nb_d), (nb_da_1_s, loigiai_nb_s)]
            list_th = [(th_da_1_d, loigiai_th_d), (th_da_1_s, loigiai_th_s)]
            list_vd = [(vd_da_1_d, loigiai_vd_d), (vd_da_1_s, loigiai_vd_s)]
            list_vdc = [(vdc_da_1_d, loigiai_vdc_d), (vdc_da_1_s, loigiai_vdc_s)]

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb = random.choice(list_nb)
                th = random.choice(list_th)
                vd = random.choice(list_vd)
                vdc = random.choice(list_vdc)

                answers = [nb[0], th[0], vd[0], vdc[0]]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (Đảm bảo câu hỏi đi kèm đúng với lời giải tương ứng)
            list_nb_1 = [nb[0]]
            list_nb_2 = [nb[1]]

            list_th_1 = [th[0]]
            list_th_2 = [th[1]]

            list_vd_1 = [vd[0]]
            list_vd_2 = [vd[1]]

            list_vdc_1 = [vdc[0]]
            list_vdc_2 = [vdc[1]]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
            str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

