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


def bt_dang29_p1_b3_c2_hh11(self):
            # Khai báo biến
            # Để góc là 45 độ, ta cần (BD * tan_SBO) / AC = 1

            list_scenarios = [
                {'BD': 4, 'AC': 2, 'p': 1, 'q': 2, 'ans': '45^\\circ'}, # Bài gốc
                {'BD': 6, 'AC': 2, 'p': 1, 'q': 3, 'ans': '45^\\circ'},
                {'BD': 4, 'AC': 4, 'p': 1, 'q': 1, 'ans': '45^\\circ'},
                {'BD': 8, 'AC': 4, 'p': 1, 'q': 2, 'ans': '45^\\circ'},
            ]

            scenario = random.choice(list_scenarios)

            # Gán giá trị từ kịch bản
            bd_val = scenario['BD']
            ac_val = scenario['AC']
            p = scenario['p']
            q = scenario['q']
            dap_an_dung = scenario['ans']

            # Tính toán các bước trung gian cho lời giải
            bo_val = Rational(bd_val, 2)
            oc_val = Rational(ac_val, 2)
            # SO = BO * tan(SBO) = (bd_val/2) * (p/q)
            so_num = bd_val * p
            so_den = 2 * q
            so_frac = Rational(so_num, so_den)

            # Chuỗi latex cho tan
            tan_sbo_tex = '\\frac{' + str(p) + '}{' + str(q) + '}' if q != 1 else str(p)

            # Các phương án nhiễu
            all_angles = ['$30^\\circ$', '$45^\\circ$', '$60^\\circ$', '$75^\\circ$', '$90^\\circ$']
            da_d = '\\True $' + dap_an_dung + '$'
            s = [angle for angle in all_angles if angle != '$' + dap_an_dung + '$']
            random.shuffle(s)
            da_s1, da_s2, da_s3 = s[0], s[1], s[2]

            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Vẽ hình TikZ
            tikz_code = (
                '\\begin{center}\n'
                '\\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, line width=1pt]\n'
                '\\coordinate (O) at (0,0);\n'
                '\\coordinate (A) at (-2,0.6);\n'
                '\\coordinate (C) at (2,-0.6);\n'
                '\\coordinate (B) at (-1,-1);\n'
                '\\coordinate (D) at (1,1);\n'
                '\\coordinate (S) at (0,3);\n'
                '\\draw [dashed] (S)--(O) (A)--(C) (S)--(D) (C)--(D) (B)--(D) (A)--(D) ;\n'
                '\\draw (S)--(B) (S)--(C) (A)--(B) (S)--(A) (B)--(C) ;\n'
                '\\foreach \\p/\\pos in {S/above, A/left, B/below left, C/below right, D/right, O/below}\n'
                '\\fill (\\p)  node[\\pos] {$\\p$};\n'
                '\\end{tikzpicture}\n'
                '\\end{center}'
            )

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Cho hình thoi $ABCD$ tâm $O$ có $BD = ' + str(bd_val) + 'a, AC = ' + str(ac_val) + 'a$. '
                'Lấy điểm $S$ không thuộc mặt phẳng $(ABCD)$ sao cho $SO \\perp (ABCD)$. '
                'Biết $\\tan \\widehat{SBO} = ' + tan_sbo_tex + '$. Góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$ bằng'
            )

            # Lời giải chi tiết
            loigiai = (
                'Vì $SO \\perp (ABCD)$ tại $O$ nên $O$ là hình chiếu vuông góc của $S$ lên mặt phẳng $(ABCD)$. \\\\'
                'Do đó, góc giữa đường thẳng $SC$ và mặt phẳng $(ABCD)$ là góc giữa $SC$ và $OC$, chính là góc $\\widehat{SCO}$. \\\\'
                'Ta có $BD = ' + str(bd_val) + 'a \\Rightarrow BO = \\frac{BD}{2} = ' + str(bo_val) + 'a$. \\\\'
                'Xét tam giác $SOB$ vuông tại $O$, ta có: \\\\'
                '$SO = BO \\cdot \\tan \\widehat{SBO} = ' + str(bo_val) + 'a \\cdot ' + tan_sbo_tex + ' = ' + (latex(so_frac) if so_frac != 1 else '') + 'a$. \\\\'
                'Ta lại có $AC = ' + str(ac_val) + 'a \\Rightarrow OC = \\frac{AC}{2} = ' + str(oc_val) + 'a$. \\\\'
                'Xét tam giác $SOC$ vuông tại $O$, ta có: \\\\'
                '$\\tan \\widehat{SCO} = \\frac{SO}{OC} = \\frac{' + latex(so_frac) + 'a}{' + str(oc_val) + 'a} = 1$. \\\\'
                'Vậy $\\widehat{SCO} = 45^\\circ$.'
            )

            # Xuất nội dung theo cấu trúc yêu cầu
            content = (
                '\\begin{minipage}{\\textwidth}\n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\choice\n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content

