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


def bt_dang22_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số k cho a (từ 1 đến 9)
                # Cạnh hình vuông sẽ là 2*k*a
                k = randint(1, 9)
                side_coeff = 2 * k

                # Tính toán các đại lượng
                # Diện tích đáy: (2ka)^2 = 4k^2 * a^2
                dt_day_coeff = side_coeff**2

                # Chiều cao SH: Tam giác đều cạnh 2ka có chiều cao (2ka*sqrt(3))/2 = k*a*sqrt(3)
                sh_coeff = k

                # Thể tích: V = 1/3 * (4k^2 * a^2) * (k*a*sqrt(3)) = (4/3 * k^3) * a^3 * sqrt(3)
                v_num = 4 * (k**3)
                v_den = 3
                v_frac = Rational(v_num, v_den)

                # Các đáp án trắc nghiệm
                # Đúng: (4k^3/3) * a^3 * sqrt(3)
                da_dung = '$' + latex(v_frac) + 'a^3\\sqrt{3}$'

                # Sai 1: 4k^3 * a^3 * sqrt(3) (Quên chia 3)
                sai1 = '$' + latex(v_num) + 'a^3\\sqrt{3}$'

                # Sai 2: (k^3/2) * a^3 * sqrt(3)
                sai2 = '$\\frac{' + latex(k**3) + 'a^3\\sqrt{3}}{2}$'

                # Sai 3: (k^3/4) * a^3 * sqrt(3)
                sai3 = '$\\frac{' + latex(k**3) + 'a^3\\sqrt{3}}{4}$'

                # Kiểm tra trùng lặp và xáo trộn
                list_ans = [('\\True ' + da_dung), sai1, sai2, sai3]
                random.shuffle(list_ans)

                # TikZ code vẽ hình giống 100% ảnh mẫu
                # Sử dụng tọa độ để mô phỏng hình chóp có mặt bên vuông góc đáy
                tikz_code = (
                    '\\begin{center} \\begin{tikzpicture}[line cap=round,line join=round,>=stealth,x=1.0cm,y=1.0cm, line width=1pt]\n'
                    '\\coordinate (B) at (0,0);\n'
                    '\\coordinate (C) at (3.5,-0.5);\n'
                    '\\coordinate (A) at (1.2,1.5);\n'
                    '\\coordinate (D) at ($(A)+(C)-(B)$);\n'
                    '\\coordinate (H) at ($(A)!0.5!(B)$);\n'
                    '\\coordinate (S) at ($(H)+(0,3.5)$);\n'
                    '\\draw [dashed] (S)--(A) (A)--(B) (A)--(D) (S)--(H);\n'
                    '\\draw (S)--(B)--(C)--(D)--(S)--(C);\n'
                    '\\draw (B) node[below left]{$B$} (C) node[below right]{$C$} (D) node[right]{$D$} (A) node[above left]{$A$} (S) node[above]{$S$} (H) node[below]{$H$};\n'
                    '\\draw [dashed] (1.2,1.35) -- (1.35,1.4) -- (1.35,1.55);\n' 
                    '\\tkzMarkRightAngle[size=0.2](S,H,A)\n' 
                    '\\end{tikzpicture} \\end{center}'
                )

                # Nội dung câu hỏi
                noidungcauhoi = (
                    'Cho hình chóp $S.ABCD$ có đáy là hình vuông cạnh bằng $%sa$. Mặt bên $\\left(SAB\\right)$ là tam giác đều và nằm trong mặt phẳng vuông góc với mặt phẳng $\\left(ABCD\\right)$. Thể tích của khối chóp $S.ABCD$ là'
                    % (latex(side_coeff))
                )

                # Nội dung lời giải
                loigiai = (
                    'Gọi $H$ là trung điểm của $AB$, ta có $SH \\perp AB$.\\\\\n'
                    'Mà $\\left(SAB\\right) \\perp \\left(ABCD\\right)$ theo giao tuyến là đường thẳng $AB$ nên $SH \\perp \\left(ABCD\\right)$.\\\\\n'
                    'Diện tích hình vuông $ABCD$ là: $S_{ABCD} = \\left(%sa\\right)^2 = %sa^2$.\\\\\n'
                    'Chiều cao khối chóp là: $SH = \\frac{%sa\\sqrt{3}}{2} = %sa\\sqrt{3}$.\\\\\n'
                    'Thể tích khối chóp $S.ABCD$ bằng $V = \\frac{1}{3} S_{ABCD} \\cdot SH = \\frac{1}{3} \\cdot %sa^2 \\cdot %sa\\sqrt{3} = %s$.'
                    % (latex(side_coeff), latex(dt_day_coeff), 
                       latex(side_coeff), latex(sh_coeff),
                       latex(dt_day_coeff), latex(sh_coeff), da_dung.replace('$', ''))
                )

            # Xuất câu trắc nghiệm
            content = (
                '\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'
                + str(noidungcauhoi) + '\n'
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + tikz_code+ str(loigiai) + '}\n'
                '\\end{ex}\n'
                '\\end{minipage} \n\n')
            return content

