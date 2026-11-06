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


def bt_dang37_p1_b3_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang=random.choice(lisdang)

            if dang=='1':
                # Chọn ngẫu nhiên hằng số a khác 0 để tạo bài toán dạng (x - a) / sqrt(x^2 - a^2)
                a = random.choice([-4, -3, -2, -1, 1, 2, 3, 4])
                a2 = a**2

                # Định dạng hiển thị chuỗi tử số và mẫu số
                if a < 0:
                    str_tu = "x + %s" % abs(a)
                else:
                    str_tu = "x - %s" % a

                str_mau = "x^2 - %s" % a2

                # Xác định các chuỗi giới hạn cho lời giải chi tiết
                if a > 0:
                    str_lim_not_tcd = "\\lim\\limits_{x \\to %s^+} f(x) = 0" % latex(a)
                else:
                    str_lim_not_tcd = "\\lim\\limits_{x \\to %s^-} f(x) = 0" % latex(a)

                if -a > 0:
                    str_lim_tcd = "\\lim\\limits_{x \\to %s^+} f(x) = +\\infty" % latex(-a)
                else:
                    str_lim_tcd = "\\lim\\limits_{x \\to %s^-} f(x) = -\\infty" % latex(-a)

                # Đáp án đúng luôn luôn là 3 tiệm cận (2 tiệm cận ngang và 1 tiệm cận đứng)
                da = '$3$'

                # Tạo các phương án nhiễu ngẫu nhiên không trùng với đáp án đúng
                options = [0, 1, 2, 4, 5]
                random.shuffle(options)

                das1 = '$%s$' % options[0]
                das2 = '$%s$' % options[1]
                das3 = '$%s$' % options[2]

                # Câu hỏi
                noidungcauhoi = ('''Đồ thị hàm số $f(x) = \\frac{%s}{\\sqrt{%s}}$ có tất cả bao nhiêu tiệm cận đứng và tiệm cận ngang?''' % (str_tu, str_mau))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Lời giải chi tiết đầy đủ các bước
                loigiai = ('''Tập xác định của hàm số là $D = (-\\infty; -%s) \\cup (%s; +\\infty)$. \\\\
            Xét các đường tiệm cận ngang: \\\\
            + Ta có $\\lim\\limits_{x \\to +\\infty} f(x) = \\lim\\limits_{x \\to +\\infty} \\frac{%s}{\\sqrt{%s}} = 1 \\Rightarrow y = 1$ là một đường tiệm cận ngang. \\\\
            + Ta có $\\lim\\limits_{x \\to -\\infty} f(x) = \\lim\\limits_{x \\to -\\infty} \\frac{%s}{\\sqrt{%s}} = -1 \\Rightarrow y = -1$ là một đường tiệm cận ngang. \\\\
            Do đó, đồ thị hàm số có $2$ đường tiệm cận ngang. \\\\
            Xét các đường tiệm cận đứng (là các nghiệm của phương trình mẫu số $x^2 - %s = 0 \\Leftrightarrow x = %s$ hoặc $x = %s$): \\\\
            + Tại $x = %s$: Ta có $%s$ nên đường thẳng $x = %s$ không phải là tiệm cận đứng của đồ thị hàm số. \\\\
            + Tại $x = %s$: Ta có $%s$ nên đường thẳng $x = %s$ là một đường tiệm cận đứng của đồ thị hàm số. \\\\
            Do đó, đồ thị hàm số có $1$ đường tiệm cận đứng. \\\\
            Vậy đồ thị hàm số có tất cả $2 + 1 = 3$ đường tiệm cận đứng và tiệm cận ngang.''' % (
                    latex(abs(a)), latex(abs(a)),
                    str_tu, str_mau,
                    str_tu, str_mau,
                    a2, latex(a), latex(-a),
                    latex(a), str_lim_not_tcd, latex(a),
                    latex(-a), str_lim_tcd, latex(-a)
                ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\choice \n'
                '{'+str(list_1[1])+'}\n'
                '{'+str(list_1[2])+'}\n'
                '{'+str(list_1[3])+'}\n'
                '{'+str(list_1[0])+'}\n'
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

