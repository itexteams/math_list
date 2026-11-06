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


def bt_dang33_p1_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến ký hiệu
            a, x = symbols('a x')

            # B3: Suy nghĩ tìm cách random bài toán
            # Random hệ số của đường chéo AC' = m * a * sqrt(3)
            m = random.randint(1, 5)

            # Giá trị đề bài கு cho AC'
            ac_val_expr = m * a * sqrt(3)
            ac_val_latex = latex(ac_val_expr)

            # Tính toán các giá trị cho lời giải
            ac_sq_val = 3 * (m**2) * (a**2) # AC'^2
            edge_val = m * a               # Cạnh x
            volume_val = (m**3) * (a**3)   # Thể tích V

            # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            # Đáp án đúng
            da_dung = '$V = %s$' % (latex(volume_val))

            # Các đáp án nhiễu (dựa trên cấu trúc các phương án trong ảnh)
            s1 = '$V = %s$' % (latex(Rational(3, 4) * sqrt(6) * (m**3) * (a**3)))
            s2 = '$V = %s$' % (latex(3 * sqrt(3) * (m**3) * (a**3)))
            s3 = '$V = %s$' % (latex(Rational(1, 3) * (m**3) * (a**3)))

            # Đảm bảo không trùng (trong trường hợp m đặc biệt, dù ở đây m nguyên dương nên hiếm trùng)
            options_set = {s1, s2, s3}
            if da_dung in options_set:
                options_set.remove(da_dung)
                # Thêm phương án thay thế nếu trùng
                options_set.add('$V = %s$' % (latex(2 * (m**3) * (a**3))))

            list_wrong = list(options_set)
            da_s1 = list_wrong[0]
            da_s2 = list_wrong[1]
            da_s3 = list_wrong[2]

            # Nội dung câu hỏi
            noidungcauhoi = (
                'Thể tích $V$ của khối lập phương $ABCD.A\'B\'C\'D\'$, biết $AC\' = %s$ bằng'
                % (ac_val_latex)
            )

            # Hình vẽ TikZ giống 100% trong ảnh với độ dày 1pt
            tikz_figure = (r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]    (92.47,168.4) -- (212.47,168.4) ;
            		\draw [line width=1]    (92.47,68.4) -- (212.47,68.4) ;
            		\draw [line width=1]    (92.47,168.4) -- (92.47,68.4) ;
            		\draw [line width=1]    (212.47,168.4) -- (212.47,68.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (132.47,28.4) ;
            		\draw [line width=1]    (252.47,128.4) -- (252.47,28.4) ;
            		\draw [line width=1]    (132.47,28.4) -- (252.47,28.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (132.47,128.4) -- (252.47,128.4) ;
            		\draw [line width=1]    (92.47,68.4) -- (132.47,28.4) ;
            		\draw [line width=1]    (212.47,68.4) -- (252.47,28.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,168.4) -- (132.47,128.4) ;
            		\draw [line width=1]    (212.47,168.4) -- (252.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,168.4) -- (252.47,128.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (92.47,68.4) -- (252.47,128.4) ;
            		\draw (73,53) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (124,6) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (255,13) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (212.47,68.4) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (75,166) node [anchor=north west][inner sep=0.75pt]    {$A'$};
            		\draw (110,112) node [anchor=north west][inner sep=0.75pt]    {$B'$};
            		\draw (256,115) node [anchor=north west][inner sep=0.75pt]    {$C'$};
            		\draw (212.47,168.4) node [anchor=north west][inner sep=0.75pt]    {$D'$};
            	\end{tikzpicture}
            \end{center}'''
            )

            # Nội dung lời giải chi tiết
            loigiai = (
                'Giả sử khối lập phương có cạnh bằng $x; \\left(x > 0\\right)$.\\\\\n'
                'Xét tam giác $A\'B\'C\'$ vuông cân tại $B\'$ ta có:\\\\\n'
                '$A\'C\'^2 = A\'B\'^2 + B\'C\'^2 = x^2 + x^2 = 2x^2 \\Rightarrow A\'C\' = x\\sqrt{2}$.\\\\\n'
                'Xét tam giác $A\'AC\'$ vuông tại $A\'$ ta có:\\\\\n'
                '$AC\'^2 = A\'A^2 + A\'C\'^2 \\Leftrightarrow %s = x^2 + 2x^2 \\Leftrightarrow x = %s$.\\\\\n'
                'Thể tích của khối lập phương $ABCD.A\'B\'C\'D\'$ là $V = %s$.'
                % (latex(ac_sq_val), latex(edge_val), latex(volume_val)))

            # Trộn đáp án
            da_d = '\\True ' + da_dung
            list_1 = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_1)

            # Xuất kết quả theo mẫu content (không dùng raw string r)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\n\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' +tikz_figure + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

