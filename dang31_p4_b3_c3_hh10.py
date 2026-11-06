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


def bt_dang31_p4_b3_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Để kết quả thường là số nguyên đẹp (bỏ .0), ta dùng các bộ số Pythagore
                # Mỗi bộ: (oa, ob, ab)
                bo_so = [(3, 4, 5), (6, 8, 10), (5, 12, 13), (9, 12, 15), (8, 15, 17), (12, 16, 20), (10, 24, 26)]
                chon = random.choice(bo_so)

                # Hệ số nhân ngẫu nhiên
                k = random.randint(1, 2)
                oa = chon[0] * k
                ob = chon[1] * k
                ab = chon[2] * k

                # Tính bán kính r = (oa + ob - ab) / 2
                # Dùng nsimplify để biến 4.0 thành 4, giúp loại bỏ dấu thập phân .0
                r_val = (oa + ob - ab) / 2
                r = nsimplify(r_val)

                tam_x = r
                tam_y = r
                r_binh = nsimplify(r**2)

                # Biến ký hiệu
                x, y = symbols('x y')

                # Phương trình đường tròn (Đáp án đúng)
                da_dung = f"$(x - {latex(tam_x)})^2 + (y - {latex(tam_y)})^2 = {latex(r_binh)}$"

                # Tạo các đáp án nhiễu
                s = [
                    f"$(x + {latex(tam_x)})^2 + (y + {latex(tam_y)})^2 = {latex(r_binh)}$",
                    f"$(x - {latex(tam_x)})^2 + (y - {latex(tam_y)})^2 = {latex(nsimplify(2*r))}$",
                    f"$(x - {latex(oa)})^2 + (y - {latex(ob)})^2 = {latex(r_binh)}$",
                    f"$(x + {latex(tam_x)})^2 + (y - {latex(tam_y)})^2 = {latex(r_binh)}$",
                ]

                # Câu hỏi
                noidungcauhoi = (f"Cho hai điểm $A({oa};0), B(0;{ob})$. Lập phương trình đường tròn nội tiếp tam giác $OAB$.")

                # Trộn đáp án
                da_d = '\\True ' + da_dung
                list_1 = [da_d, s[0], s[1], s[2]]
                random.shuffle(list_1)

                # Nội dung lời giải (Sử dụng nsimplify cho mọi giá trị số để mất đuôi .0)
                loigiai = (f"Ta có $OA = {oa}; OB = {ob}; AB = \\sqrt{{{oa}^2 + {ob}^2}} = {ab}$. \\\\\n"
                           f"Mặt khác $\\frac{{1}}{{2}}OA \\cdot OB = p \\cdot r$ (vì cùng bằng diện tích tam giác $OAB$). \\\\\n"
                           f"Suy ra $r = \\frac{{OA \\cdot OB}}{{OA + OB + AB}} = \\frac{{{oa} \\cdot {ob}}}{{{oa} + {ob} + {ab}}} = {latex(r)}$. \\\\\n"
                           f"Dễ thấy đường tròn cần tìm có tâm thuộc góc phần tư thứ nhất và tiếp xúc với hai trục tọa độ nên tâm của đường tròn có tọa độ là $I({latex(tam_x)}; {latex(tam_y)})$. \\\\\n"
                           f"Vậy phương trình đường tròn nội tiếp tam giác $OAB$ là $({latex(x)} - {latex(tam_x)})^2 + ({latex(y)} - {latex(tam_y)})^2 = {latex(r_binh)}$.")

                # Xử lý hiển thị dấu
                loigiai = loigiai.replace("- -", "+ ").replace("+ -", "- ")

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

