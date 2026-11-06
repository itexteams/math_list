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


def bt_dang36_p3_b3_c3_ds12(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 3: Random các thông số bài toán
                # Giả sử h là độ sâu (đỉnh parabol xuống trục hoành)
                # Giả sử w là nửa chiều rộng của miệng máng (giao điểm với trục hoành tại x = w và x = -w)
                h = random.randint(2, 6) 
                w = random.randint(1, 4)

                # Phương trình parabol dạng y = ax^2 - h
                # Tại x = w thì y = 0 => a*w^2 - h = 0 => a = h / w^2
                a_val = Rational(h, w**2)

                # Tính diện tích S = tích phân từ -w đến w của (0 - (ax^2 - h)) dx = (h - ax^2) dx
                # S = 4/3 * h * w
                S_val = Rational(4, 3) * h * w

                # Kết quả làm tròn đến hàng phần chục (1 chữ số thập phân)
                kq_float = float(S_val)
                kq_rounded = Decimal(str(kq_float)).quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
                kq_str = str(kq_rounded).replace('.', ',')

                # Bước 4: Tạo các phương án sai (không trùng đáp án đúng)
                da_dung = '$%s$' % kq_str

                s = []
                offsets = [-1.5, -1.0, -0.5, 0.5, 1.0, 1.5, 2.0]
                random.shuffle(offsets)

                for offset in offsets:
                    sai_val = float(kq_rounded) + offset
                    if sai_val > 0:
                        sai_str = '$%s$' % (str(round(sai_val, 1)).replace('.', ','))
                        if sai_str != da_dung and sai_str not in s:
                            s.append(sai_str)
                    if len(s) == 3:
                        break

                das1, das2, das3 = s

                # Nội dung câu hỏi
                noidungcauhoi = (r'''\immini{Mặt cắt ngang của lòng máng dẫn nước là hình phẳng giới hạn bởi một parabol và đường thẳng nằm ngang như Hình (phần được tô màu). Biết chiều sâu của lòng máng là $%s$m và chiều rộng của miệng máng là $%s$m. Diện tích của mặt cắt ngang đó bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).}
                                 {\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (108,53.9) -- (245.6,53.9) -- (245.6,190.5) -- (108,190.5) -- cycle ;
            	\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (233.44,43.69) .. controls (231.27,120.98) and (206.85,181.9) .. (177.05,181.9) .. controls (147.22,181.9) and (122.79,120.88) .. (120.65,43.49) -- cycle ;
            	\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (88.5,13) -- (253.1,13) -- (253.1,53) -- (88.5,53) -- cycle ;
            	\draw    (158.5,54.5) -- (229.1,54.89) ;
            	\draw [shift={(231.1,54.9)}, rotate = 180.32] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            	\draw    (158.5,54.5) -- (125.6,54.5) ;
            	\draw [shift={(123.6,54.5)}, rotate = 360] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            	\draw    (260.6,111.9) -- (260.6,180.9) ;
            	\draw [shift={(260.6,182.9)}, rotate = 270] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            	\draw  [dash pattern={on 4.5pt off 4.5pt}]  (178.6,181.9) -- (245.6,182.4) ;
            	\draw    (260.6,111.9) -- (260.6,56.4) ;
            	\draw [shift={(260.6,54.4)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            	\draw (160.5,27) node [anchor=north west][inner sep=0.75pt]    {$%s$ m};
            	\draw (269,106) node [anchor=north west][inner sep=0.75pt]    {$%s$ m};
            \end{tikzpicture}}'''
                                 % (latex(h), latex(2*w),latex(2*w), latex(h)))

                # Nội dung lời giải
                # Sử dụng \text{d}x theo yêu cầu
                loigiai = (r'''\begin{center}
            				\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1] 
            					\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (108,53.9) -- (245.6,53.9) -- (245.6,190.5) -- (108,190.5) -- cycle ;
            					\draw  [fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (233.44,43.69) .. controls (231.27,120.98) and (206.85,181.9) .. (177.05,181.9) .. controls (147.22,181.9) and (122.79,120.88) .. (120.65,43.49) -- cycle ;
            					\draw  [color={rgb, 255:red, 255; green, 255; blue, 255 }  ,draw opacity=1 ][fill={rgb, 255:red, 255; green, 255; blue, 255 }  ,fill opacity=1 ] (88.5,13) -- (253.1,13) -- (253.1,53) -- (88.5,53) -- cycle ;
            					\draw    (91.52,54.16) -- (277.52,53.76) ;
            					\draw [shift={(279.52,53.76)}, rotate = 179.88] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw    (177,209.36) -- (177,21.6) ;
            					\draw [shift={(177,19.6)}, rotate = 90] [color={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.75]    (10.93,-3.29) .. controls (6.95,-1.4) and (3.31,-0.3) .. (0,0) .. controls (3.31,0.3) and (6.95,1.4) .. (10.93,3.29)   ;
            					\draw (157.4,53.8) node [anchor=north west][inner sep=0.75pt]    {$O$};
            					\draw (262.2,66) node [anchor=north west][inner sep=0.75pt]    {$x$};
            					\draw (158.2,15.2) node [anchor=north west][inner sep=0.75pt]    {$y$};
            					\draw (153.8,154.8) node [anchor=north west][inner sep=0.75pt]    {$-%s$};
            					\draw (104.6,28.8) node [anchor=north west][inner sep=0.75pt]    {$-%s$};
            					\draw (225,29.2) node [anchor=north west][inner sep=0.75pt]    {$%s$};
            				\end{tikzpicture}
            			\end{center} Chọn hệ trục tọa độ $Oxy$ có trục hoành nằm dọc theo cạnh trên của mặt cắt ngang, trục tung đi qua đỉnh của parabol. Khi đó, đường parabol có phương trình dạng $y = ax^2 - %s$ ($a > 0$). \\
                           Theo giả thiết, miệng máng rộng $%s$m nên parabol đi qua điểm $(%s; 0)$, ta có: \\
                           $a \cdot (%s)^2 - %s = 0 \Leftrightarrow a = %s$. \\
                           Suy ra phương trình của parabol là $y = %sx^2 - %s$. \\
                           Diện tích mặt cắt của cống là: \\
                           $S = \int_{-%s}^{%s} \left[0 - \left(%sx^2 - %s \right) \right] \text{d}x = \int_{-%s}^{%s} (%s - %sx^2) \text{d}x$ \\
                           $= \left( %sx - \frac{%sx^3}{3} \right) \Big|_{-%s}^{%s} = %s \approx %s \text{ (m}^2\text{)}$.'''
                           % (latex(h),latex(w),latex(w),latex(h), latex(2*w), latex(w), latex(w), latex(h), latex(a_val),
                              latex(a_val), latex(h), 
                              latex(w), latex(w), latex(a_val), latex(h),
                              latex(w), latex(w), latex(h), latex(a_val),
                              latex(h), latex(a_val), latex(w), latex(w), latex(S_val), kq_str))
                #Đáp án
                dapan='\\shortans[0]{$%s$}\n'%(kq_str)

                # Đưa các đáp án vào danh sách
                da_d = '\\True ' + da_dung
                list_1 = [da_d, das1, das2, das3]
                random.shuffle(list_1)

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ str(dapan)+
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

