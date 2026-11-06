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


def bt_dang68_p4_b2_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến và chọn dạng (giữ nguyên cấu trúc mẫu)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # B3: Suy nghĩ tìm cách random bài toán
                # d phải là số chẵn để x = d/2 là số nguyên cho đẹp
                # h thường nhỏ hơn d nhiều
                d_val = randint(2, 6) * 2  # Đường kính d (ví dụ: 4, 6, 8, 10, 12)
                h_val = random.choice([0.5, 1, 1.5, 2]) # Chiều cao h

                # Tính toán: y = ax^2. Tại x = d/2 thì y = h
                # h = a * (d/2)^2 => a = h / (d/2)^2
                x_val = Rational(d_val , 2)
                a_frac = Rational(str(h_val)) / (Rational(x_val)**2)

                m = a_frac.p # Tử số
                n = a_frac.q # Mẫu số

                # Đáp án đúng
                kq_dung = m - n

                # B4: Điều chỉnh các phương án sai không được phép trùng với đáp án đúng
                du = [str(kq_dung)]
                da = kq_dung

                s = set()
                while len(s) < 3:
                    # Tạo các giá trị sai quanh đáp án đúng
                    sai = kq_dung + randint(-10, 10)
                    if sai != kq_dung:
                        s.add(str(sai))

                list_sai = list(s)
                das1, das2, das3 = list_sai[0], list_sai[1], list_sai[2]

                # Nội dung câu hỏi
                noidungcauhoi = (r'''Một chiếc ăng - ten chảo parabol có chiều cao $h = %sm$ và đường kính miệng $d = %sm$. Mặt cắt qua trục là một parabol dạng $y = ax^2$. Biết $a = \frac{m}{n}$, trong đó $m, n$ là các số nguyên dương nguyên tố cùng nhau. Tính $m - n$.'''
                                % (latex(h_val), latex(d_val)))

                # Hình vẽ TikZ
                # Tính tọa độ để vẽ
                x_draw = 2 # scale cố định cho hình vẽ
                y_draw = 1
                tik_picture = (r'''\begin{center}
            \begin{tikzpicture}[scale=0.8, >=stealth]
                \draw[->] (-2.5,0) -- (2.5,0) node[below] {$x$};
                \draw[->] (0,-0.5) -- (0,2) node[right] {$y$};
                \draw[thick,blue] plot[domain=-2:2] (\x, {0.25*(\x)^2});
                \draw[dashed] (-2,0) -- (-2,1) -- (2,1) -- (2,0);
                \node at (0,0) [below left] {$O$};
                \node at (2,0) [below] {$%s$};
                \node at (-2,0) [below] {$-%s$};
                \node at (0,1) [above right] {$%s$};
            \end{tikzpicture}
            \end{center}''' % (latex(x_val), latex(x_val), latex(h_val)))

                # Các đáp án
                da_d = ('\\True $' + str(da) + '$')
                da_s1 = '$' + str(das1) + '$'
                da_s2 = '$' + str(das2) + '$'
                da_s3 = '$' + str(das3) + '$'

                list_1 = [da_d, da_s1, da_s2, da_s3]
                random.shuffle(list_1)

                # Nội dung lời giải chi tiết
                loigiai = (r'''%s 
            Từ giả thiết, đường kính miệng $d = %s$m nên bán kính miệng là $x = \frac{%s m}{2} = %s$m. \\
            Khi đó, parabol đi qua điểm $I\left( %s; %s \right)$. \\
            Thay tọa độ điểm $I$ vào phương trình $y = ax^2$, ta có: \\
            $%s = a \cdot (%s)^2 \Leftrightarrow  %s = a \cdot %s \Leftrightarrow  a = \frac{%s}{%s} = \frac{m}{n}$. \\
            Vì $m, n$ là các số nguyên dương nguyên tố cùng nhau nên $m = %s, n = %s$. \\
            Vậy $m - n = %s - %s = %s$.''' 
                           % (tik_picture, latex(d_val), latex(d_val), latex(x_val), 
                              latex(x_val), latex(h_val).replace('.',','), 
                              latex(h_val), latex(x_val), latex(h_val), latex(x_val**2), 
                              latex(m), latex(n), 
                              latex(m), latex(n), 
                              latex(m), latex(n), latex(kq_dung)))

            # Xuất câu trắc nghiệm (Giữ nguyên cấu trúc mẫu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
                '\\loigiai{'+str(loigiai)+'}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

