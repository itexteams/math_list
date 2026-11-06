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


def bt_dang3_p3_b2_c2_hh11(self):
            # Khai báo biến
            # B3- Suy nghĩ tìm cách random bài toán
            # Random hệ số k trong SA = a*sqrt(k). Bài gốc k = 3.
            lis_k = [1, 2, 3, 4, 5, 7, 9]
            k = random.choice(lis_k)

            # Tính toán các giá trị
            # SA^2 = k*a^2, AB^2 = a^2 => SB^2 = (k+1)a^2
            # Tỉ số SM/SB = SA^2/SB^2 = k / (k+1)
            ti_so_frac = Rational(k, k + 1)
            kq_float = float(ti_so_frac)

            # Định dạng kết quả số thập phân, thay dấu chấm bằng dấu phẩy
            def format_decimal(val):
                d = Decimal(str(float(val))).quantize(Decimal('1.0'), rounding=ROUND_HALF_UP).normalize()
                return str(d).replace('.', ',')

            kq = format_decimal(kq_float)

            # B4- Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
            def generate_distractors(correct_val):
                distractors = set()
                while len(distractors) < 3:
                    # Tạo các giá trị sai quanh đáp án đúng
                    offset = random.choice([-0.25, -0.15, 0.1, 0.2, 0.3, -0.1])
                    wrong_val = float(correct_val) + offset
                    if wrong_val > 0 and wrong_val < 1:
                        fmt_wrong = format_decimal(wrong_val)
                        if fmt_wrong != kq:
                            distractors.add(fmt_wrong)
                return list(distractors)

            wrong_answers = generate_distractors(kq_float)

            # Thiết lập chuỗi LaTeX cho SA
            if k == 1:
                sa_latex = "a"
            else:
                sa_latex = "a\\sqrt{" + str(k) + "}"

            # TikZ code - Vẽ hình giống 100% ảnh (độ dày 1pt, đúng các nét đứt)
            # M được tính toán vị trí trên SB dựa theo tỉ số k/(k+1)
            m_ratio = float(k) / (k + 1)
            tikz_code = r'''\begin{center}
            	\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            		\draw [line width=1]    (190.47,181.4) -- (254.47,182.4) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (154.47,129.4) -- (316.47,129.4) ;
            		\draw [line width=1]    (190.47,181.4) -- (154.47,129.4) ;
            		\draw [line width=1]    (254.47,182.4) -- (316.47,129.4) ;
            		\draw [line width=1]    (154.47,129.4) -- (153.47,24.4) ; 
            		\draw [line width=1]    (153.47,24.4) -- (316.47,129.4) ;
            		\draw [line width=1]    (153.47,24.4) -- (254.47,182.4) ; 
            		\draw [line width=1]    (153.47,24.4) -- (190.47,181.4) ;
            		\draw [line width=1]    (154.47,129.4) -- (171.97,102.9) ;
            		\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (190.47,181.4) -- (316.47,129.4) ;
            		\draw [line width=1]    (316.47,129.4) -- (171.97,102.9) ;
            		\draw (146,0) node [anchor=north west][inner sep=0.75pt]    {$S$};
            		\draw (136,118) node [anchor=north west][inner sep=0.75pt]    {$A$};
            		\draw (175,177) node [anchor=north west][inner sep=0.75pt]    {$B$};
            		\draw (254.47,182.4) node [anchor=north west][inner sep=0.75pt]    {$C$};
            		\draw (318,118) node [anchor=north west][inner sep=0.75pt]    {$D$};
            		\draw (171,80) node [anchor=north west][inner sep=0.75pt]    {$M$};
            	\end{tikzpicture}
            \end{center}'''

            # B2- Viết nội dung câu hỏi và lời giải
            noidungcauhoi = ("Cho hình chóp $S.ABCD$ có đáy $ABCD$ là nửa lục giác đều với cạnh $a$. Cạnh $SA$ vuông góc với đáy và $SA = %s$. $M$ là một điểm khác $B$ và ở trên $SB$ sao cho $AM$ vuông góc với $MD$. Khi đó, tỉ số $\\frac{SM}{SB}$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục)." 
                             % (sa_latex))


            # Nội dung lời giải chi tiết
            loigiai = ("Áp dụng tính chất nửa lục giác đều cạnh $a$, ta có $AD = 2a$ và $BD \\perp AB$.\\\\ "
                       "Mà hình chiếu vuông góc của đường thẳng $AM$ lên $\\left( ABCD \\right)$ là $AB$.\\\\ "
                       "Vậy $BD \\perp AM$.\\\\ "
                       "Kết hợp $AM \\perp MD$, ta được $AM \\perp \\left( SBD \\right)$. Suy ra $AM \\perp SB$.\\\\ "
                       "Khi đó, trong tam giác vuông $SAB$ với đường cao $AM$, ta có:\\\\ "
                       "$\\frac{SM}{SB} = \\frac{SM \\cdot SB}{SB^2} = \\frac{SA^2}{SA^2 + AB^2} = \\frac{%s a^2}{%s a^2 + a^2} = \\frac{%s}{%s} = %s$."
                       % (str(k), str(k), str(k), str(k+1), kq))
            #Đáp án
            dapan='\\shortans[0]{$%s$}\n'%(kq)
            # Các đáp án
            da_d = ("\\True " + kq)
            da_s1 = wrong_answers[0]
            da_s2 = wrong_answers[1]
            da_s3 = wrong_answers[2]

            list_ans = [da_d, da_s1, da_s2, da_s3]
            random.shuffle(list_ans)

            # Xuất câu trắc nghiệm theo mẫu
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + str(dapan)+
                '\\loigiai{' +tikz_code + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

