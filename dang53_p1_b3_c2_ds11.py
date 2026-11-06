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


def bt_dang53_p1_b3_c2_ds11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                loai_csn = random.choice([1, 2])

                if loai_csn == 1:
                    # BC, AH, AB lập thành CSN
                    day_csn = "độ dài cạnh đáy $BC$, đường cao $AH$ và cạnh bên $AB$"
                    pt_str = "(a \\cdot q^2)^2 = (a \\cdot q)^2 + \\left(\\frac{a}{2}\\right)^2"
                    pt_rut_gon = "q^4 = q^2 + \\frac{1}{4} \\Leftrightarrow 4q^4 - 4q^2 - 1 = 0"
                    delta_str = "(-4)^2 - 4 \\cdot 4 \\cdot (-1) = 32"
                    t_res = "\\frac{4 + \\sqrt{32}}{8} = \\frac{4 + 4\\sqrt{2}}{8} = \\frac{1 + \\sqrt{2}}{2}"

                    kq = "\\frac{\\sqrt{2} + 1}{2}"
                    fake1 = "\\frac{\\sqrt{2} - 1}{2}"
                    fake2 = "\\frac{2 + \\sqrt{2}}{2}"
                    fake3 = "\\frac{2 - \\sqrt{2}}{2}"

                    goi_str = "Gọi $BC = a \\ (a > 0)$. Theo giả thiết $BC, AH, AB$ lập thành cấp số nhân với công bội $q \\ (q > 0)$, ta có: $AH = a \\cdot q$, $AB = a \\cdot q^2$."
                    bien_doi = "\\frac{a}{2}"

                else:
                    # BH, AH, AB lập thành CSN
                    day_csn = "độ dài nửa cạnh đáy $BH$, đường cao $AH$ và cạnh bên $AB$"
                    pt_str = "(a \\cdot q^2)^2 = (a \\cdot q)^2 + a^2"
                    pt_rut_gon = "q^4 = q^2 + 1 \\Leftrightarrow q^4 - q^2 - 1 = 0"
                    delta_str = "(-1)^2 - 4 \\cdot 1 \\cdot (-1) = 5"
                    t_res = "\\frac{1 + \\sqrt{5}}{2}"

                    kq = "\\frac{\\sqrt{5} + 1}{2}"
                    fake1 = "\\frac{\\sqrt{5} - 1}{2}"
                    fake2 = "\\frac{2 + \\sqrt{5}}{2}"
                    fake3 = "\\frac{2 - \\sqrt{5}}{2}"

                    goi_str = "Gọi $BH = a \\ (a > 0)$. Theo giả thiết $BH, AH, AB$ lập thành cấp số nhân với công bội $q \\ (q > 0)$, ta có: $AH = a \\cdot q$, $AB = a \\cdot q^2$."
                    bien_doi = "a"


                # Các đáp án trắc nghiệm
                du = ['$%s$' % kq]
                da = random.choice(du)
                s = [
                    '$%s$' % fake1,
                    '$%s$' % fake2,
                    '$%s$' % fake3
                ]

                das1 = s[0]
                das2 = s[1]
                das3 = s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho tam giác $ABC$ cân tại đỉnh $A$, biết %s theo thứ tự lập thành cấp số nhân với công bội $q$. Giá trị của $q^2$ bằng''' % day_csn)

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải
                loigiai = ('''%s\\\\
                            Trong tam giác $ABC$ cân tại $A$, $AH$ là đường cao nên $AH$ cũng là đường trung tuyến, suy ra $H$ là trung điểm của $BC$.\\\\
                            Xét tam giác $ABH$ vuông tại $H$, ta có: $AB^2 = AH^2 + BH^2$.\\\\
                            Suy ra: $%s \\Rightarrow %s$.\\\\
                            Đặt $t = q^2 \\ (t > 0)$. Phương trình trở thành phương trình bậc hai đối với $t$.\\\\
                            Ta tính được $t = %s$ (thỏa mãn) hoặc $t < 0$ (loại).\\\\
                            Vậy $q^2 = %s$.'''
                           % (goi_str, pt_str, pt_rut_gon, t_res, kq))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{\n'+str(loigiai)+'\n}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

