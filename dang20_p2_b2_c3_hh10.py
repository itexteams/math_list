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


def bt_dang20_p2_b2_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y, m = symbols('x y m')

            # B1 & B3: Nghiên cứu đề bài và tìm cách random
            # Chọn ngẫu nhiên tọa độ A(xA; 0) và B(0; yB) để tạo ra các tam giác vuông đẹp
            # Thường chọn các cặp (3,4), (6,8), (5,12)
            pairs = [(4, 3), (3, 4), (8, 6), (6, 8), (12, 5), (5, 12)]
            xA, yB = random.choice(pairs)

            # Các thông số tính toán
            AB_len_sq = xA**2 + yB**2
            AB_len = sqrt(AB_len_sq)

            # Phương trình đường thẳng AB: yB*x + xA*y - xA*yB = 0
            coef_x = yB
            coef_y = xA
            const_term = -xA * yB

            # Đường thẳng Delta: mx + 2y - 5 = 0 vuông góc với AB
            # Vectơ chỉ phương AB là (xA, -yB), Vectơ chỉ phương Delta là (2, -m)
            # Vuông góc <=> 2*xA + (-m)*(-yB) = 0 <=> 2*xA + m*yB = 0 <=> m = -2*xA/yB
            m_val = Rational(-2 * xA, yB)

            # Điểm M(a; 0) trên Ox, I là trung điểm AB => I(xA/2; yB/2)
            # MI vuông góc AB: vec(MI).(xA; -yB) = 0 
            # (xA/2 - a)*xA + (yB/2)*(-yB) = 0 <=> xA^2/2 - a*xA - yB^2/2 = 0
            # a = (xA^2 - yB^2) / (2*xA)
            a_val = Rational(xA**2 - yB**2, 2 * xA)
            b_val = 0 # Vì M nằm trên Ox
            sum_val = a_val + b_val**2

            # Nội dung câu hỏi
            noidungcauhoi = r'''Trong mặt phẳng với hệ tọa độ $Oxy$, cho hai điểm $A\left(%s;0\right)$ và $B\left(0;%s\right)$.''' % (xA, yB)

            ########################################################################
            # a) Nhận biết: Độ dài đoạn thẳng AB
            nb_da_1_d = r'\True Độ dài đoạn thẳng $AB$ bằng $%s$' % (latex(AB_len))
            nb_da_1_s = r'Độ dài đoạn thẳng $AB$ bằng $%s$' % (latex(AB_len + 1)) # Sai số
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = r'''Ta có $AB = \sqrt{\left(0-%s\right)^2 + \left(%s-0\right)^2} = %s$.''' % (xA, yB, latex(AB_len))

            ########################################################################
            # b) Thông hiểu: Phương trình đường thẳng AB
            th_da_1_d = r'\True Đường thẳng đi qua hai điểm $A$ và $B$ có phương trình là $%sx + %sy %s = 0$' % (coef_x, coef_y, const_term)
            th_da_1_s = r'Đường thẳng đi qua hai điểm $A$ và $B$ có phương trình là $%sx + %sy + %s = 0$' % (coef_x, coef_y, abs(const_term))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = r'''Phương trình đường thẳng $AB$ theo đoạn chắn là $\frac{x}{%s} + \frac{y}{%s} = 1 \Leftrightarrow %sx + %sy %s = 0$.''' % (xA, yB, coef_x, coef_y, const_term)

            ########################################################################
            # c) Vận dụng: Điều kiện vuông góc
            vd_da_1_d = r'\True Đường thẳng $\Delta : mx + 2y - 5 = 0$ vuông góc với đường thẳng $AB$ khi $m = %s$' % (latex(m_val))
            vd_da_1_s = r'Đường thẳng $\Delta : mx + 2y - 5 = 0$ vuông góc với đường thẳng $AB$ khi $m = %s$' % (latex(-m_val))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = r'''Đường thẳng $AB$ có vectơ chỉ phương $\vec{u}_{AB} = \left(-%s; %s\right)$. Đường thẳng $\Delta$ có vectơ pháp tuyến $\vec{n}_{\Delta} = \left(m; 2\right) \Rightarrow \vec{u}_{\Delta} = \left(2; -m\right)$. \\
            Để $AB \perp \Delta$ thì $\vec{u}_{AB} \cdot \vec{u}_{\Delta} = 0 \Leftrightarrow -%s \cdot 2 + %s \cdot \left(-m\right) = 0 \Leftrightarrow m = %s$.''' % (xA, yB, xA, yB, latex(m_val))

            ########################################################################
            # d) Vận dụng cao: Điểm M trên trục hoành
            vdc_da_1_d = r'\True Điểm $M\left(a;b\right)$ nằm trên trục hoành $Ox$ sao cho $MI \perp AB$, khi đó $a + b^2 = %s$' % (latex(sum_val))
            vdc_da_1_s = r'Điểm $M\left(a;b\right)$ nằm trên trục hoành $Ox$ sao cho $MI \perp AB$, khi đó $a + b^2 = %s$' % (latex(sum_val + 1))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = r'''Vì $M \in Ox$ nên $M\left(a; 0\right)$, suy ra $b = 0$. \\
            $I$ là trung điểm $AB$ nên $I\left(\frac{%s}{2}; \frac{%s}{2}\right)$. Ta có $\vec{MI} = \left(\frac{%s}{2} - a; \frac{%s}{2}\right)$ và $\vec{AB} = \left(-%s; %s\right)$. \\
            $MI \perp AB \Leftrightarrow \vec{MI} \cdot \vec{AB} = 0 \Leftrightarrow -%s\left(\frac{%s}{2} - a\right) + %s \cdot \frac{%s}{2} = 0 \Leftrightarrow a = %s$. \\
            Vậy $a + b^2 = %s$.''' % (xA, yB, xA, yB, xA, yB, xA, xA, yB, yB, latex(a_val), latex(sum_val))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 câu đúng
            while True:
                da_nb = random.choice(list_nb_da_1)
                da_th = random.choice(list_th_da_1)
                da_vd = random.choice(list_vd_da_1)
                da_vdc = random.choice(list_vdc_da_1)

                if 1 <= count_true_answers([da_nb, da_th, da_vd, da_vdc]) <= 3:
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n'
                '\\choiceTFn \n'
                '{' + da_nb + '}\n'
                '{' + da_th + '}\n'
                '{' + da_vd + '}\n'
                '{' + da_vdc + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + loigiai_nb_1 + '\n'
                '\\item ' + loigiai_th_1 + '\n'
                '\\item ' + loigiai_vd_1 + '\n'
                '\\item ' + loigiai_vdc_1 + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n\n')
            return content   

