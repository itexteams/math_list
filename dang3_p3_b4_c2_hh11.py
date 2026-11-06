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


def bt_dang3_p3_b4_c2_hh11(self):
            # Khai báo biến
            # alpha là góc SOA, kq_goc là góc nhị diện [S, BD, C] = 180 - alpha
            sets = [
                {'a': 2, 'h_tex': '\\sqrt{6}', 'alpha': 60, 'kq_goc': 120},
                {'a': 2, 'h_tex': '\\sqrt{2}', 'alpha': 45, 'kq_goc': 135},
                {'a': 4, 'h_tex': '2\\sqrt{6}', 'alpha': 60, 'kq_goc': 120},
                {'a': 4, 'h_tex': '2\\sqrt{2}', 'alpha': 45, 'kq_goc': 135},
                {'a': 6, 'h_tex': '\\sqrt{6}', 'alpha': 30, 'kq_goc': 150}
            ]

            data = random.choice(sets)
            a = data['a']
            h_tex = data['h_tex']
            alpha = data['alpha']
            kq_goc = data['kq_goc']

            # Tính toán các giá trị trung gian cho lời giải
            ao_tex = latex(Rational(a, 2)) + '\\sqrt{2}'
            tan_val_tex = '1' if alpha == 45 else ('\\sqrt{3}' if alpha == 60 else '\\frac{\\sqrt{3}}{3}')

            # Tạo danh sách đáp án
            da_dung = '$' + str(kq_goc) + '^{\\circ}$'
            cac_lua_chon = [120, 135, 150, 60, 45, 30, 90]
            if kq_goc in cac_lua_chon:
                cac_lua_chon.remove(kq_goc)

            random.shuffle(cac_lua_chon)
            s1 = '$' + str(cac_lua_chon[0]) + '^{\\circ}$'
            s2 = '$' + str(cac_lua_chon[1]) + '^{\\circ}$'
            s3 = '$' + str(cac_lua_chon[2]) + '^{\\circ}$'

            da_d = '\\True ' + da_dung
            list_1 = [da_d, s1, s2, s3]
            random.shuffle(list_1)

            # Nội dung câu hỏi
            noidungcauhoi = ('Cho hình chóp tứ giác $S.ABCD$ có đáy $ABCD$ là hình vuông cạnh bằng $' + str(a) + '$. '
                             'Biết rằng $SA$ vuông góc với mặt phẳng $\\left(ABCD\\right)$ và $SA = ' + h_tex + '$ (tham khảo hình vẽ). '
                             'Góc phẳng nhị diện $[S, BD, C]$ có số đo bằng bao nhiêu độ?')

            # Hình vẽ TikZ
            tikz_code = (
                '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                '\\coordinate (A) at (0,0);\n'
                '\\coordinate (B) at (4,0);\n'
                '\\coordinate (D) at (-1.5,-1.5);\n'
                '\\coordinate (C) at ($(B)+(D)-(A)$);\n'
                '\\coordinate (S) at (0,4);\n'
                '\\coordinate (O) at ($(A)!0.5!(C)$);\n'
                '\\draw (S)--(D)--(C)--(B)--(S)--(C);\n'
                '\\draw [dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O);\n'
                '\\node [left] at (A) {$A$};\n'
                '\\node [right] at (B) {$B$};\n'
                '\\node [right] at (C) {$C$};\n'
                '\\node [below] at (D) {$D$};\n'
                '\\node [above] at (S) {$S$};\n'
                '\\node [below] at (O) {$O$};\n'
                '\\end{tikzpicture}'
            )

            # Lời giải chi tiết
            loigiai = ('Gọi $O$ là giao điểm của $AC$ và $BD$. Vì $ABCD$ là hình vuông nên $AC \\perp BD$ tại $O$. \\\\ \n'
                       'Ta có: $\\begin{cases} BD \\perp AC \\\\ BD \\perp SA \\text{ (vì } SA \\perp \\left(ABCD\\right) \\text{ ) } \\end{cases} '
                       '\\Rightarrow BD \\perp \\left(SAC\\right) \\Rightarrow BD \\perp SO$ và $BD \\perp OC$. \\\\ \n'
                       'Khi đó, góc phẳng nhị diện $[S, BD, C]$ là góc $\\widehat{SOC}$. \\\\ \n'
                       'Xét tam giác vuông $SAO$ tại $A$, ta có $AO = \\frac{1}{2}AC = \\frac{' + str(a) + '\\sqrt{2}}{2} = ' + ao_tex + '$. \\\\ \n'
                       '$\\tan \\widehat{SOA} = \\frac{SA}{AO} = \\frac{' + h_tex + '}{' + ao_tex + '} = ' + tan_val_tex + ' \\Rightarrow \\widehat{SOA} = ' + str(alpha) + '^{\\circ}$. \\\\ \n'
                       'Vì $A, O, C$ thẳng hàng và $O$ nằm giữa $A, C$ nên $\\widehat{SOC} = 180^{\\circ} - \\widehat{SOA} = 180^{\\circ} - ' + str(alpha) + '^{\\circ} = ' + str(kq_goc) + '^{\\circ}$.')
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(latex(kq_goc))
            # Xuất nội dung theo cấu trúc yêu cầu
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n'
                       + str(noidungcauhoi) + '\n'
                       '\\begin{center}\n'
                       + tikz_code + '\n'
                       '\\end{center}\n'+str(dapan)+
                       '\\loigiai{' + str(loigiai) + '}\n'
                       '\\end{ex}\n'
                       '\\end{minipage} \n')
            return content                   

