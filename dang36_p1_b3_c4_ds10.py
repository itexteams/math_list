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


def bt_dang36_p1_b3_c4_ds10(self):
            # Khai báo biến
            # B1 & B2: Thiết lập biến và giải bài toán gốc
            x = symbols('x')

            # Tạo các hệ số ngẫu nhiên cho bất phương trình ax^2 + bx + c >= 0
            # Để có nghiệm đẹp như trong hình (nghiệm nguyên), ta chọn 2 nghiệm x1, x2
            x1 = random.randint(1, 3)
            x2 = random.randint(5, 9)

            # Khai triển (x - x1)(x - x2) = x^2 - (x1+x2)x + x1*x2
            a = 1
            b = -(x1 + x2)
            c = x1 * x2

            # Bất phương trình: x^2 + bx + c >= 0
            f = a*x**2 + b*x + c
            sol = solveset(f >= 0, x, domain=S.Reals)

            # Tập nghiệm S dưới dạng Latex để hiển thị
            S_latex = latex(sol)

            # B3 & B4: Tạo các phương án trắc nghiệm
            # Đáp án đúng (Không là tập con của S) phải chứa một phần của khoảng (x1, x2)
            # Ta chọn một khoảng [m, +inf) sao cho m nằm giữa x1 và x2 (ví dụ x1 < m < x2)
            m_wrong = random.randint(x1 + 1, x2 - 1)
            da_dung = '[%s; +\\infty)' % m_wrong

            # Các phương án sai (thực chất là tập con của S)
            s1 = '$(-\\infty; %s]$' % (x1 - random.randint(0, 2))
            s2 = '$[%s; +\\infty)$' % (x2 + random.randint(0, 2))
            s3 = '$(-\\infty; %s]$' % (x1 - 3)

            # Danh sách các phương án
            list_ans = [
                '\\True $' + da_dung+'$',
                s1,
                s2,
                s3
            ]
            random.shuffle(list_ans)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Gọi $S$ là tập nghiệm của bất phương trình $%s \\ge 0$. Trong các tập hợp sau, tập nào \\textbf{không} là tập con của $S$?'''
                            % (latex(f)))

            # Nội dung lời giải chi tiết
            loigiai = ('''Ta có $%s \\ge 0 \\Leftrightarrow  \\left[ \\begin{aligned} & x \\le %s \\\\ & x \\ge %s \\end{aligned} \\right.$. \\\\
                         Suy ra tập nghiệm của bất phương trình là $S = %s$. \\\\
                         Xét tập hợp $%s$: Ta thấy có phần tử $x$ thỏa mãn $%s < x < %s$ thuộc tập hợp này nhưng không thuộc $S$. \\\\
                         Do đó $%s \\not\\subset S$.'''
                         % (latex(f), x1, x2, S_latex, da_dung, x1, x2, da_dung))

            # Xuất câu trắc nghiệm theo định dạng yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

