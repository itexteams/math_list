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


def bt_dang26_p1_b3_c3_ds12(self):
            # Khai báo biến
            triples = [
                (4, 3, 5),   # Gốc trong đề bài
                (8, 6, 10),
                (12, 5, 13),
                (15, 8, 17),
                (12, 9, 15),
                (24, 7, 25)
            ]

            d, r, R = random.choice(triples)

            # Bước 2: Viết lại bài toán theo mẫu
            x = symbols('x')


            f2_sq = r**2 - (x - d)**2
            f1_sq = R**2 - x**2

            # Tính toán thể tích V
            V_part2 = integrate(f2_sq, (x, d, d + r))
            V_part1 = integrate(f1_sq, (x, d, R))
            V_final = pi * (V_part2 - V_part1)

            # Chuyển sang dạng Latex
            latex_V = latex(V_final)

            # Bước 4: Tạo các phương án sai không trùng đáp án đúng
            def generate_distractors(correct_val):
                results = set()
                results.add('$%s$' % latex_V)

                # Tạo các biến thể sai (thay đổi tử số hoặc mẫu số)
                num, den = correct_val.as_numer_denom()
                # Loại bỏ pi khỏi num để tính toán số
                num_val = int(num / pi)

                offsets = [10, -10, 20, 5, -5, 15]
                random.shuffle(offsets)

                for offset in offsets:
                    if len(results) >= 4:
                        break
                    wrong_num = abs(num_val + offset)
                    wrong_latex = latex(Rational(wrong_num, den)).replace('pi', '') + '\\pi'
                    results.add('$%s$' % wrong_latex)

                res_list = list(results)
                # Tìm vị trí đáp án đúng để gắn \True
                final_list = []
                for item in res_list:
                    if item == '$%s$' % latex_V:
                        final_list.append('\\True ' + item)
                    else:
                        final_list.append(item)
                return final_list

            list_ans = generate_distractors(V_final)
            random.shuffle(list_ans)


            # Nội dung câu hỏi
            noidungcauhoi = r"""\immini{Cho hai đường tròn $(O_1; %s)$ và $(O_2; %s)$ cắt nhau tại hai điểm $A, B$ sao cho $AB$ là một đường kính của đường tròn $(O_2; %s)$. Gọi $(D)$ là phần hình phẳng giới hạn bởi hai đường tròn (ở ngoài đường tròn lớn, phần tô dấu chấm như hình vẽ). Quay $(D)$ quanh trục $O_1O_2$ ta được một khối tròn xoay. Thể tích $V$ của khối tròn xoay được tạo thành là}
            {\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            				\draw   (135.82,157.54) .. controls (136.53,116.9) and (170.05,84.54) .. (210.69,85.25) .. controls (251.32,85.95) and (283.69,119.47) .. (282.98,160.11) .. controls (282.28,200.75) and (248.76,233.12) .. (208.12,232.41) .. controls (167.48,231.7) and (135.11,198.18) .. (135.82,157.54) -- cycle ;
            				\draw   (224,159.53) .. controls (224,134.98) and (243.91,115.07) .. (268.47,115.07) .. controls (293.02,115.07) and (312.93,134.98) .. (312.93,159.53) .. controls (312.93,184.09) and (293.02,204) .. (268.47,204) .. controls (243.91,204) and (224,184.09) .. (224,159.53) -- cycle ;
            				\draw    (268.47,115.07) -- (268.47,204) ;
            				\draw    (135.47,160.89) -- (312.93,159.53) ;
            				\draw (262,87) node [anchor=north west][inner sep=0.75pt]    {$A$};
            				\draw (266.47,201) node [anchor=north west][inner sep=0.75pt]    {$B$};
            				\draw (183.33,135.47) node [anchor=north west][inner sep=0.75pt]    {$O_{1}$};
            				\draw (244,136.8) node [anchor=north west][inner sep=0.75pt]    {$O_{2}$};
            				\draw (287.33,136.8) node [anchor=north west][inner sep=0.75pt]    {$(D)$};
            			\end{tikzpicture}}""" % (R, r, r,)

            # Lời giải chi tiết
            loigiai = r"""\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            					\draw    (99.47,160.07) -- (342.13,159.34) ;
            					\draw [shift={(344.13,159.33)}, rotate = 179.83] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw    (209.47,243.56) -- (209.47,50.07) ;
            					\draw [shift={(209.47,48.07)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw   (135.82,157.54) .. controls (136.53,116.9) and (170.05,84.54) .. (210.69,85.25) .. controls (251.32,85.95) and (283.69,119.47) .. (282.98,160.11) .. controls (282.28,200.75) and (248.76,233.12) .. (208.12,232.41) .. controls (167.48,231.7) and (135.11,198.18) .. (135.82,157.54) -- cycle ;
            					\draw   (224,159.53) .. controls (224,134.98) and (243.91,115.07) .. (268.47,115.07) .. controls (293.02,115.07) and (312.93,134.98) .. (312.93,159.53) .. controls (312.93,184.09) and (293.02,204) .. (268.47,204) .. controls (243.91,204) and (224,184.09) .. (224,159.53) -- cycle ;
            					\draw    (268.47,115.07) -- (268.47,204) ;
            					\draw (262,87) node [anchor=north west][inner sep=0.75pt]    {$A$};
            					\draw (266.47,201) node [anchor=north west][inner sep=0.75pt]    {$B$};
            					\draw (183.33,135.47) node [anchor=north west][inner sep=0.75pt]    {$O_{1}$};
            					\draw (244,136.8) node [anchor=north west][inner sep=0.75pt]    {$O_{2}$};
            					\draw (287.33,136.8) node [anchor=north west][inner sep=0.75pt]    {$(D)$};
            					\draw (332,140) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (194,41.47) node [anchor=north west][inner sep=0.75pt]    {$y$};
            				\end{tikzpicture}
            			\end{center}
                        Chọn hệ tọa độ sao cho $O_1$ trùng gốc tọa độ, trục $Ox$ đi qua $O_1, O_2$. \\
            Khi đó phương trình các đường tròn là:\\
            $(O_1): x^2 + y^2 = %s \Rightarrow y^2 = %s - x^2$.\\
            $(O_2): (x - %s)^2 + y^2 = %s \Rightarrow y^2 = %s - (x - %s)^2$.\\
            Vì $AB$ là đường kính của $(O_2)$ và $AB \perp O_1O_2$ nên hoành độ giao điểm $A, B$ là $x = %s$.\\
            Phần hình phẳng $(D)$ khi quay quanh $Ox$ tạo ra thể tích:\\
            $V = \pi \int_{%s}^{%s} \left[ %s - (x - %s)^2 \right] \text{d}x - \pi \int_{%s}^{%s} \left[ %s - x^2 \right] \text{d}x$.\\
            Tính toán ta được $V = %s$.""" % (R**2, R**2, d, r**2, r**2, d, d, d, d+r, r**2, d, d, R, R**2, latex_V)

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) + 
                '\\choice \n'
                '{' + str(list_ans[0]) + '}\n'
                '{' + str(list_ans[1]) + '}\n'
                '{' + str(list_ans[2]) + '}\n'
                '{' + str(list_ans[3]) + '}\n'
                '\\loigiai{' + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

