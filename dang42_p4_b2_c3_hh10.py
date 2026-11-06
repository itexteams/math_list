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


def bt_dang42_p4_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # 1. Khởi tạo các biến ký hiệu
                x, y = symbols('x y')

                # 2. Random điểm M và điểm B sao cho tọa độ nguyên
                xm, ym = randint(-3, 5), randint(-3, 5)
                xb, yb = randint(-5, 8), randint(-5, 8)
                while (xm == xb and ym == yb): 
                    xb, yb = randint(-5, 8), randint(-5, 8)

                # Tính tọa độ điểm A (M là trung điểm AB: A = 2M - B)
                xa, ya = 2*xm - xb, 2*ym - yb

                # 3. Tạo phương trình d1, d2 đi qua M: a(x-xm) + b(y-ym) = 0
                a1, b1 = randint(-3, 4), randint(-3, 4)
                while a1 == 0 and b1 == 0: a1, b1 = randint(-3, 4), randint(-3, 4)
                c1 = -(a1*xm + b1*ym)

                a2, b2 = randint(-3, 4), randint(-3, 4)
                while (a2 == 0 and b2 == 0) or (a1*b2 == a2*b1): # Đảm bảo không song song
                    a2, b2 = randint(-3, 4), randint(-3, 4)
                c2 = -(a2*xm + b2*ym)

                # Các biểu thức đường thẳng d1, d2
                d1_expr = a1*x + b1*y + c1
                d2_expr = a2*x + b2*y + c2

                # 4. Trường hợp 1: d1 // BC, d2 // AC
                c_bc1 = -(a1*xb + b1*yb)
                bc1_expr = a1*x + b1*y + c_bc1
                c_ac1 = -(a2*xa + b2*ya)
                ac1_expr = a2*x + b2*y + c_ac1

                sol1 = solve([bc1_expr, ac1_expr], (x, y))
                xc1, yc1 = sol1[x], sol1[y]

                # 5. Trường hợp 2: d1 // AC, d2 // BC
                c_ac2 = -(a1*xa + b1*ya)
                ac2_expr = a1*x + b1*y + c_ac2
                c_bc2 = -(a2*xb + b2*yb)
                bc2_expr = a2*x + b2*y + c_bc2

                sol2 = solve([ac2_expr, bc2_expr], (x, y))
                xc2, yc2 = sol2[x], sol2[y]

                # Hàm định dạng tọa độ với \left( và \right)
                def fmt(vx, vy):
                    return "\\left(" + latex(vx) + ";" + latex(vy) + "\\right)"

                # Đáp án đúng
                da_dung = "$%s$ và $%s$" % (fmt(xc1, yc1), fmt(xc2, yc2))

                # Phương án nhiễu (Đảm bảo không trùng đáp án đúng)
                s = [
                    "$%s$ và $%s$" % (fmt(xc1+1, yc1), fmt(xc2, yc2-1)),
                    "$%s$ và $%s$" % (fmt(xc1, yc1+2), fmt(xc2-1, yc2)),
                    "$%s$" % (fmt(xc1, yc1)),
                    "$%s$" % (fmt(xc2, yc2)),
                    "$%s$ và $%s$" % (fmt(yc1, xc1), fmt(yc2, xc2)),
                ]
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Trong mặt phẳng với hệ tọa độ $Oxy$, cho tam giác $ABC$ có hai đường trung bình kẻ từ trung điểm $M$ của $AB$ nằm trên các đường thẳng có phương trình $d_1 : %s = 0, d_2 : %s = 0$ và tọa độ điểm $B%s$. Tìm tọa độ điểm $C$.'''
                                 %(latex(d1_expr), latex(d2_expr), fmt(xb, yb)))

                # Các đáp án
                da_d = ('\\True ' + str(da_dung))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Lời giải chi tiết sử dụng \parallel
                loigiai = ('''Tọa độ trung điểm $M(x;y)$ của $AB$ là giao điểm của $d_1$ và $d_2$, thỏa mãn hệ phương trình:
            $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Rightarrow M%s$.\\\\
            Vì $M$ là trung điểm của $AB$ nên ta có tọa độ điểm $A = 2M - B = %s$.\\\\
            Vì hai đường thẳng đã cho là các đường trung bình kẻ từ $M$ nên chúng song song với các cạnh của tam giác đối diện.\\\\
            \\textbf{TH1:} Giả sử $d_1 \\parallel BC$ và $d_2 \\parallel AC$.\\\\
            $\\bullet$ Đường thẳng $AC$ đi qua $A%s$ và song song với $d_2$ nên có phương trình: $%s = 0$.\\\\
            $\\bullet$ Đường thẳng $BC$ đi qua $B%s$ và song song với $d_1$ nên có phương trình: $%s = 0$.\\\\
            Tọa độ $C = AC \\cap BC$ là nghiệm của hệ:
            $\\begin{cases} %s = 0 \\\\ %s = 0 \\end{cases} \\Rightarrow C%s$.\\\\
            \\textbf{TH2:} Giả sử $d_1 \\parallel AC$ và $d_2 \\parallel BC$.\\\\
            Tương tự TH1, ta tìm được tọa độ điểm $C%s$.\\\\
            Vậy tọa độ điểm $C$ là $%s$ hoặc $%s$.'''
                %(latex(d1_expr), latex(d2_expr), fmt(xm, ym), fmt(xa, ya),
                  fmt(xa, ya), latex(ac1_expr), fmt(xb, yb), latex(bc1_expr),
                  latex(ac1_expr), latex(bc1_expr), fmt(xc1, yc1),
                  fmt(xc2, yc2), fmt(xc1, yc1), fmt(xc2, yc2)
                ))

            # Xuất nội dung (Không dùng raw string r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content 

