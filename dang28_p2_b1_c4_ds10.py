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


def bt_dang28_p2_b1_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')
            m_val = random.randint(2, 5) # Random giá trị m cụ thể để tính toán lời giải mẫu

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho hàm số $y=f(x)=\\begin{cases} 3x-2 & \\text{khi } x \\ge 2 \\\\ 4-(m^2-1)x & \\text{khi } 0 < x < 2 \\\\ \\dfrac{x-3}{x-1} & \\text{khi } x \\le 0 \\end{cases}$.''')

            ########################################################################
            # Nhận biết 
            ########################################################################
            nb_da_1_d = '\\True Với $m \\in (2;+\\infty)$ thì hàm số đồng biến trên $(2;+\\infty)$'
            nb_da_1_s = 'Với $m \\in (2;+\\infty)$ thì hàm số nghịch biến trên $(2;+\\infty)$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Với $m \\in (2;+\\infty)$ thì trên khoảng $(2;+\\infty)$ hàm số có dạng $f(x)=3x-2$. Đây là hàm bậc nhất có hệ số $a=3 > 0$ nên hàm số đồng biến trên $(2;+\\infty)$.''')

            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu 
            ########################################################################
            th_da_1_d = '\\True Hàm số đã cho không nghịch biến trên khoảng $(0;3)$'
            th_da_1_s = 'Hàm số đã cho nghịch biến trên khoảng $(0;3)$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Xét trên khoảng $(0;3)$: \\\\
            - Với $0 < x < 2$: $f(x)=4-(m^2-1)x$. Nếu $0 < m < 2$ thì $m^2-1$ có thể dương, hàm số nghịch biến. \\\\
            - Với $2 \\le x < 3$: $f(x)=3x-2$ có $a=3 > 0$ nên hàm số đồng biến. \\\\
            Vì trên khoảng $(0;3)$ hàm số có khoảng đồng biến nên hàm số không thể nghịch biến trên $(0;3)$.''')

            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng 
            ########################################################################
            vd_da_1_d = '\\True Có vô số giá trị nguyên của tham số $m$ để hàm số nghịch biến trên $(0;2)$'
            vd_da_1_s = 'Có 2 giá trị nguyên của tham số $m$ để hàm số nghịch biến trên $(0;2)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Trên khoảng $(0;2)$, hàm số là $f(x)=4-(m^2-1)x$. \\\\
            Hàm số nghịch biến trên $(0;2)$ khi và chỉ khi $m^2-1 > 0 \\Leftrightarrow \\left[ \\begin{aligned} & m > 1 \\\\ & m < -1 \\end{aligned} \\right.$. \\\\
            Do đó có vô số giá trị nguyên của tham số $m$ thỏa mãn yêu cầu bài toán.''')

            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao
            ########################################################################
            vdc_da_1_d = '\\True Với $m < 0$ và $m \\in [-3;-1]$ thì $f(m) < f(m+2)$'
            vdc_da_1_s = '\\True Với $m < 0$ và $m \\in [-3;-1]$ thì $f(m) > f(m+2)$'
            # Đổi đáp án sai cho logic
            vdc_da_1_s = vdc_da_1_s.replace('\\True', '') 

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Khi $x \\le 0$, $f(x)=\\dfrac{x-3}{x-1} = 1 - \\dfrac{2}{x-1}$. \\\\
            Đạo hàm $f\'(x) = \\dfrac{2}{(x-1)^2} > 0$ nên hàm số đồng biến trên $(-\\infty; 0]$. \\\\
            Với $m \\in [-3;-1]$ thì $m < 0$ và $m+2 \\in [-1;1]$. \\\\
            Tuy nhiên, xét tính đơn điệu và giá trị tại các đầu mút, ta thấy hàm số đồng biến trên các khoảng xác định. Khi $m < 0$ và giá trị tăng lên thì $f(m) < f(m+2)$.''')

            list_vdc_2 = [loigiai_vdc_1]

            ########################################################################
            # Xử lý chọn đáp án Đúng/Sai
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán vào list cuối cùng để in
            shuffled_answers = answers
            shuffled_solutions = [list_nb_2[0], list_th_2[0], list_vd_2[0], list_vdc_2[0]]

            # Xuất nội dung theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

