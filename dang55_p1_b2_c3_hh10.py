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


def bt_dang55_p1_b2_c3_hh10(self):
            # u2_x, u2_y là hệ số của t trong Delta 2 (VTCP)
            # Khai báo biến ký hiệu
            m = symbols('m')

            # Bước 1 & 3: Nghiên cứu đề và thiết lập logic random
            # Để M có tọa độ đẹp, ta chọn b, tọa độ A và một hệ số k trước
            # Đường thẳng d: x + by + c = 0. Vector pháp tuyến n = (1; b)
            # M là hình chiếu của A trên d khi vecto AM cùng phương với n.
            # AM = k * n = (k, kb) => M = A + (k, kb)

            b = random.randint(1, 3)
            xA = random.randint(-5, 5)
            yA = random.randint(-5, 5)
            k = random.choice([-3, -2, -1, 1, 2, 3])

            # Tọa độ điểm M tối ưu (M0)
            xM0 = xA + k
            yM0 = yA + k * b

            # Tìm c sao cho M0 thuộc d: x + by + c = 0 => c = -(xM0 + b*yM0)
            c = -(xM0 + b * yM0)

            # Thành phần phương trình đường thẳng d
            def format_line(a, b, c):
                expr = ""
                if a == 1: expr += "x"
                elif a == -1: expr += "-x"
                else: expr += str(a) + "x"

                if b > 0: expr += " + " + (str(b) if b != 1 else "") + "y"
                else: expr += " - " + (str(abs(b)) if b != -1 else "") + "y"

                if c > 0: expr += " + " + str(c)
                elif c < 0: expr += " - " + str(abs(c))
                return expr

            line_str = format_line(1, b, c)

            # Bước 2: Viết lời giải chi tiết theo tham số
            # M thuộc d => xM = -b*m - c (với yM = m)
            x_param = -b * m - c
            AM_vec_x = x_param - xA
            AM_vec_y = m - yA

            # AM^2 = (AM_vec_x)^2 + (AM_vec_y)^2
            dist_sq = expand(AM_vec_x**2 + AM_vec_y**2)
            # dist_sq có dạng Am^2 + Bm + C
            A_coeff = dist_sq.coeff(m, 2)
            B_coeff = dist_sq.coeff(m, 1)
            C_coeff = dist_sq.coeff(m, 0)

            # Tìm m_min = -B/(2A)
            m_min = Rational(-B_coeff, 2 * A_coeff)
            min_val_sq = simplify(dist_sq.subs(m, m_min))
            min_dist = sqrt(min_val_sq)

            # Tọa độ M khi đó
            x_final = x_param.subs(m, m_min)
            y_final = m_min

            # Nội dung câu hỏi
            noidungcauhoi = ("Trong mặt phẳng với hệ tọa độ $Oxy$, cho đường thẳng $d: %s = 0$ và điểm $A(%s;%s)$. Tọa độ điểm $M$ thuộc $d$ sao cho $MA$ nhỏ nhất là"
                             % (line_str, latex(xA), latex(yA)))

            # Nội dung lời giải
            # Biến đổi biểu thức bậc 2 về dạng bình phương: A(m - m_min)^2 + min_val_sq
            loigiai = ("Điểm $M \\in d$ nên có tọa độ dạng $M(%s; m)$. \\\\"
                       "Khi đó $\\overrightarrow{AM} = (%s; %s)$, suy ra $AM = \\sqrt{(%s)^2 + (%s)^2} = \\sqrt{%s}$ \\\\"
                       "Ta có $\\sqrt{%s} = \\sqrt{%s(m - %s)^2 + %s} \\ge \\sqrt{%s}$ \\\\"
                       "Dấu \"=\" xảy ra khi và chỉ khi $m = %s$ \\\\"
                       "Vậy $M(%s; %s)$ và giá trị nhỏ nhất của $AM$ bằng $\\sqrt{%s}$."
                       % (latex(x_param), latex(AM_vec_x), latex(AM_vec_y), latex(AM_vec_x), latex(AM_vec_y), latex(dist_sq),
                          latex(dist_sq), latex(A_coeff), latex(m_min), latex(min_val_sq), latex(min_val_sq),
                          latex(m_min), latex(x_final), latex(y_final), latex(min_val_sq)))

            # Bước 4: Tạo các phương án trắc nghiệm (không trùng lặp)
            da_dung = "$M(%s; %s)$" % (latex(x_final), latex(y_final))
            s = set()
            while len(s) < 3:
                # Tạo các tọa độ sai bằng cách lệch 1 vài đơn vị hoặc đảo dấu
                dx = random.randint(-2, 2)
                dy = random.randint(-2, 2)
                if dx == 0 and dy == 0: continue

                # Một cách tạo đáp án sai phổ biến là lấy các điểm khác cũng nằm trên d
                m_wrong = m_min + random.choice([-2, -1, 1, 2])
                xw = x_param.subs(m, m_wrong)
                yw = m_wrong
                ans_wrong = "$M(%s; %s)$" % (latex(xw), latex(yw))
                if ans_wrong != da_dung:
                    s.add(ans_wrong)

            list_s = list(s)
            da_s1, da_s2, da_s3 = list_s[0], list_s[1], list_s[2]

            # Đưa vào danh sách và xáo trộn
            list_all = ["\\True " + da_dung, da_s1, da_s2, da_s3]
            random.shuffle(list_all)

            # Xuất câu trắc nghiệm theo đúng format mẫu
            content = ("\\begin{minipage}{\\textwidth} \n"
                       "\\begin{ex}\n" + str(noidungcauhoi) + "\n"
                       "\\choice \n"
                       "{" + str(list_all[0]) + "}\n"
                       "{" + str(list_all[1]) + "}\n"
                       "{" + str(list_all[2]) + "}\n"
                       "{" + str(list_all[3]) + "}\n"
                       "\\loigiai{" + str(loigiai) + "}\n"
                       "\\end{ex}\n \\end{minipage} \n\n")
            return content 

