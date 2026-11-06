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


def bt_dang23_p2_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            x = symbols('x')

            # --- BƯỚC 1: SINH DỮ LIỆU NGẪU NHIÊN CHO BÀI TOÁN ---
            # Để đảm bảo lời giải đẹp, ta chọn a và b sao cho các điểm đi qua là số nguyên
            # Ở đây ta giả định một bộ số mẫu, bạn có thể mở rộng list này
            options = [
                {'a': -2, 'b': 0},
                {'a': 1, 'b': -2},
                {'a': 2, 'b': 4},
                {'a': -1, 'b': 2}
            ]
            data = random.choice(options)
            a_val = data['a']
            b_val = data['b']
            c_val = 2 # Theo đề bài c luôn bằng 2

            # Nội dung câu hỏi gốc
            noidungcauhoi = "Cho hàm số $y = ax^2 + bx + 2$ với $a \\neq 0$, có đồ thị là $(P)$."

            ########################################################################
            # Nhận biết: Đi qua 2 điểm M, N (Câu a)
            ########################################################################
            # Giả sử điểm M(1; 0) và N(-1; 0) như trong hình
            val_a_plus_2024b = a_val + 2024 * b_val
            nb_da_1_d = '\\True Biết $(P)$ đi qua hai điểm $M(1;0)$ và $N(-1;0)$. Khi đó $a+2024b = %s$' % (latex(val_a_plus_2024b))
            nb_da_1_s = 'Biết $(P)$ đi qua hai điểm $M(1;0)$ và $N(-1;0)$. Khi đó $a+2024b = %s$' % (latex(val_a_plus_2024b + 1))

            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ("$(P)$ đi qua hai điểm $M(1;0)$ và $N(-1;0)$ nên ta có hệ phương trình: " 
                            "$\\begin{cases} a(1)^2 + b(1) + 2 = 0 \\\\ a(-1)^2 + b(-1) + 2 = 0 \\end{cases} "
                            "\\Leftrightarrow \\begin{cases} a+b+2=0 \\\\ a-b+2=0 \\end{cases} "
                            "\\Leftrightarrow \\begin{cases} a=%s \\\\ b=%s \\end{cases}$. \\\\"
                            "Suy ra $a+2024b = %s + 2024(%s) = %s$." 
                            % (latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(val_a_plus_2024b)))

            ########################################################################
            # Thông hiểu: Trục đối xứng (Câu b)
            ########################################################################
            truc_dx = -Rational(b_val, 2*a_val)
            val_2a_plus_b = 2*a_val + b_val
            # Tọa độ điểm E khi x = -1
            y_E = a_val * (-1)**2 + b_val * (-1) + 2

            th_da_1_d = '\\True Biết $(P)$ đi qua điểm $E(-1;%s)$ và có trục đối xứng là $x = %s$. Khi đó $2a+b = %s$' % (latex(y_E), latex(truc_dx), latex(val_2a_plus_b))
            th_da_1_s = 'Biết $(P)$ đi qua điểm $E(-1;%s)$ và có trục đối xứng là $x = %s$. Khi đó $2a+b = 1$' % (latex(y_E), latex(truc_dx))

            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ("$(P)$ có trục đối xứng là $x = %s \\Rightarrow -\\frac{b}{2a} = %s \\Rightarrow %sa + b = 0 \\quad (1)$.\\\\ "
                            "Mặt khác $(P)$ đi qua $E(-1;%s)$ nên $a(-1)^2 + b(-1) + 2 = %s \\Leftrightarrow a-b = %s \\quad (2)$. \\\\"
                            "Từ (1) và (2) ta giải được $a=%s, b=%s$. Vậy $2a+b = 2(%s) + (%s) = %s$."
                            % (latex(truc_dx), latex(truc_dx), latex(-2*truc_dx), latex(y_E), latex(y_E), latex(y_E-2), latex(a_val), latex(b_val), latex(a_val), latex(b_val), latex(val_2a_plus_b)))

            ########################################################################
            # Vận dụng: Tung độ đỉnh (Câu c)
            ########################################################################
            delta_val = b_val**2 - 4*a_val*2
            y_dinh = -Rational(delta_val, 4*a_val)
            tich_ab = a_val * b_val
            # Tọa độ điểm F khi x = -1
            y_F = a_val * (-1)**2 + b_val * (-1) + 2

            vd_da_1_d = '\\True Biết $(P)$ đi qua điểm $F(-1;%s)$ và có tung độ đỉnh bằng $%s$. Khi đó $ab = %s$' % (latex(y_F), latex(y_dinh), latex(tich_ab))
            vd_da_1_s = 'Biết $(P)$ đi qua điểm $F(-1;%s)$ và có tung độ đỉnh bằng $%s$. Khi đó $ab = -36$' % (latex(y_F), latex(y_dinh))

            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ("$(P)$ đi qua $F(-1;%s) \\Rightarrow a-b+2=%s \\Leftrightarrow a-b=%s \\Leftrightarrow a=b+%s$. \\\\"
                            "Tung độ đỉnh $-\\frac{\\Delta}{4a} = %s \\Leftrightarrow \\frac{b^2-8a}{4a} = -%s$.\\\\ "
                            "Thay $a$ vào ta tìm được các cặp $(a,b)$. Với $a=%s, b=%s$ thì $ab=%s$."
                            % (latex(y_F), latex(y_F), latex(y_F-2), latex(y_F-2), latex(y_dinh), latex(-y_dinh), latex(a_val), latex(b_val), latex(tich_ab)))

            ########################################################################
            # Vận dụng cao: Tọa độ đỉnh S (Câu d)
            ########################################################################
            x_dinh = -Rational(b_val, 2*a_val)
            # y_dinh đã tính ở trên
            bieu_thuc_d = 2*a_val + b_val # Ví dụ tính 2a + b

            vdc_da_1_d = '\\True Biết $(P)$ có đỉnh là điểm $S(%s; %s)$. Khi đó $(2a+b) \\vdots 2$' % (latex(x_dinh), latex(y_dinh))
            vdc_da_1_s = 'Biết $(P)$ có đỉnh là điểm $S(%s; %s)$. Khi đó $(2a+b) \\vdots 7$' % (latex(x_dinh), latex(y_dinh))

            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ("Vì $(P)$ có đỉnh $S(%s;%s)$ nên hoành độ đỉnh $x_S = -\\frac{b}{2a} = %s \\Rightarrow %sa + b = 0$. \\\\"
                             "Mặt khác $S$ thuộc $(P)$ nên $a(%s)^2 + b(%s) + 2 = %s$. \\\\"
                             "Giải hệ ta được $a=%s, b=%s$. Khi đó $2a+b = %s$."
                             % (latex(x_dinh), latex(y_dinh), latex(x_dinh), latex(-2*x_dinh), latex(x_dinh), latex(x_dinh), latex(y_dinh), latex(a_val), latex(b_val), latex(val_2a_plus_b)))

            # --- BƯỚC 2: KIỂM TRA ĐIỀU KIỆN ĐÁP ÁN ĐÚNG (1-3 câu) ---
            def count_true(ans_list):
                return sum('\\True' in a for a in ans_list)

            while True:
                a1 = random.choice(list_nb_da_1)
                a2 = random.choice(list_th_da_1)
                a3 = random.choice(list_vd_da_1)
                a4 = random.choice(list_vdc_da_1)
                if 1 <= count_true([a1, a2, a3, a4]) <= 3:
                    break

            # --- BƯỚC 3: XUẤT NỘI DUNG ---
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + 
                '\n\\choiceTFn \n'
                '{' + str(a1) + '}\n'
                '{' + str(a2) + '}\n'
                '{' + str(a3) + '}\n'
                '{' + str(a4) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

