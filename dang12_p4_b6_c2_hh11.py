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


def bt_dang12_p4_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random a từ 1 đến 9
                val_a = randint(1, 9)

                # Tính toán các giá trị theo bài toán
                # AB = 2a. Ở đây ta lấy a là giá trị random, vậy AB = 2 * val_a
                canh_ab = 2 * val_a
                # Chiều cao SH của tam giác đều SAB cạnh 2a: SH = (2a * sqrt(3)) / 2 = a * sqrt(3)
                sh_val = val_a * sqrt(3)
                # Diện tích đáy ABC vuông cân tại B: S = 1/2 * AB^2 = 1/2 * (2a)^2 = 2a^2
                s_abc = 2 * (val_a**2)
                # Thể tích V = 1/3 * S_abc * SH = 1/3 * 2a^2 * a*sqrt(3) = (2/3) * a^3 * sqrt(3)
                v_val = Rational(2, 3) * (val_a**3) * sqrt(3)

                # Các phương án nhiễu dựa trên các hệ số trong ảnh (1/4, 1/3, 1/12)
                pa_1 = Rational(1, 4) * (val_a**3) * sqrt(3)
                pa_2 = Rational(1, 3) * (val_a**3) * sqrt(3)
                pa_3 = Rational(1, 12) * (val_a**3) * sqrt(3)

                # Đáp án đúng
                da = '$V = %s$' % (latex(v_val))

                # Bước 4: Đảm bảo các phương án sai không trùng đáp án đúng
                s = [
                    '$V = %s$' % (latex(pa_1)),
                    '$V = %s$' % (latex(pa_2)),
                    '$V = %s$' % (latex(pa_3)),
                    '$V = %s$' % (latex(Rational(4, 3) * (val_a**3) * sqrt(3))),
                    '$V = %s$' % (latex(val_a**3 * sqrt(3))),
                ]

                # Lọc bỏ nếu có trùng (dù với a >= 1 thì các hệ số này khác nhau)
                if da in s:
                    s.remove(da)

                das1 = random.choice(s)
                s.remove(das1)
                das2 = random.choice(s)
                s.remove(das2)
                das3 = random.choice(s)

                # Câu hỏi
                noidungcauhoi = ('Cho hình chóp $S.ABC$ có đáy $ABC$ là tam giác vuông cân tại $B$ và $AB = %s$. Tam giác $SAB$ đều và nằm trong mặt phẳng vuông góc với đáy. Tính thể tích $V$ khối chóp $S.ABC$.'
                                 % (latex(canh_ab)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                da_s1 = str(das1)
                da_s2 = str(das2) 
                da_s3 = str(das3) 

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # TikZ vẽ hình giống 100% (nét vẽ 1pt, đầy đủ các điểm và đường nối)
                tikz_hinh = (
                    '\\begin{center}\n'
                    '\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]\n'
                    '\\coordinate (A) at (0,1);\n'
                    '\\coordinate (B) at (1.5,-0.5);\n'
                    '\\coordinate (C) at (4,1);\n'
                    '\\coordinate (H) at (0.75,0.25);\n'
                    '\\coordinate (S) at (0.75,3.5);\n'
                    '\\draw[line width=1pt] (S)--(A)--(B)--(C)--(S);\n'
                    '\\draw[line width=1pt] (S)--(B);\n'
                    '\\draw[dashed, line width=1pt] (A)--(C);\n'
                    '\\draw[line width=1pt] (S)--(H);\n'
                    '\\draw[line width=1pt] (H)--(B);\n'
                    '\\filldraw (S)  node[above] {$S$};\n'
                    '\\filldraw (A)  node[left] {$A$};\n'
                    '\\filldraw (B)  node[below] {$B$};\n'
                    '\\filldraw (C)  node[right] {$C$};\n'
                    '\\filldraw (H)  node[below left] {$H$};\n'
                    '\\end{tikzpicture}\n'
                    '\\end{center}'
                )

                # Nội dung lời giải chi tiết, không viết tắt
                loigiai = (tikz_hinh + 
                           'Gọi $H$ là trung điểm của $AB$. Vì tam giác $SAB$ đều và nằm trong mặt phẳng vuông góc với đáy nên $SH \\perp \\left(ABC\\right)$ và $SH$ là chiều cao của khối chóp. \\\\ \n'
                           'Chiều cao của tam giác đều $SAB$ là $SH = \\frac{%s \\sqrt{3}}{2} = %s$. \\\\ \n'
                           'Vì tam giác $ABC$ vuông cân tại $B$ nên $BC = AB = %s$. \\\\ \n'
                           'Diện tích tam giác $ABC$ là $S_{\\Delta ABC} = \\frac{1}{2} \\cdot %s^2 = %s$. \\\\ \n'
                           'Thể tích của khối chóp $S.ABC$ là \\\\ \n'
                           '$V_{S.ABC} = \\frac{1}{3} \\cdot S_{ABC} \\cdot SH = \\frac{1}{3} \\cdot %s \\cdot %s = %s$.'
                           % (latex(canh_ab), latex(sh_val),
                              latex(canh_ab),
                              latex(canh_ab), latex(s_abc),
                              latex(s_abc), latex(sh_val), latex(v_val)
                             ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

