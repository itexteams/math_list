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


def bt_dang26_p4_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến sympy
            a = symbols('a')

            # Danh sách dạng (để mở rộng sau này)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số của AC = m*a*sqrt(2) và B'C = n*a
                # Trong đề bài mẫu: m = 1, n = 3
                m = random.randint(1, 3)
                n = random.randint(m + 2, m + 5) # Đảm bảo n > m để căn bậc 2 dương

                # Tính toán các thông số
                # AC = m*a*sqrt(2) => BC = m*a
                val_AC = m * sqrt(2) * a
                val_BC = m * a

                # BB' = sqrt(B'C^2 - BC^2) = sqrt((n*a)^2 - (m*a)^2) = a * sqrt(n^2 - m^2)
                h_sq = n**2 - m**2
                val_BB_prime = sqrt(h_sq) * a

                # Diện tích đáy S = 1/2 * BC^2 (do tam giác vuông cân tại B)
                val_S = Rational(1, 2) * (m**2) * (a**2)

                # Thể tích theo logic lời giải trong ảnh (Sử dụng 1/3 diện tích đáy * chiều cao)
                # V = 1/3 * BB' * S
                val_V = simplify(Rational(1, 3) * val_BB_prime * val_S)

                # Đáp án đúng
                da = '$V = %s$' % (latex(val_V).replace('.', ','))

                # Tạo các đáp án sai
                s = [
                    '$V = %s$' % (latex(simplify(val_V * 2)).replace('.', ',')),
                    '$V = %s$' % (latex(simplify(val_V * Rational(1, 2))).replace('.', ',')),
                    '$V = %s$' % (latex(simplify(val_V + a**3)).replace('.', ',')),
                    '$V = %s$' % (latex(simplify(val_V * sqrt(3))).replace('.', ',')),
                    '$V = %s$' % (latex(simplify(val_V * 3)).replace('.', ',')),
                ]

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi
                noidungcauhoi = ('''Cho khối lăng trụ đứng $ABC.A'B'C'$ có $B'C = %s$, đáy $ABC$ là tam giác vuông cân tại $B$ và $AC = %s$. Tính thể tích khối lăng trụ đứng $ABC.A'B'C'$.'''
                                 % (latex(n*a), latex(val_AC)))

                # Các đáp án cho vào list
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # TikZ code vẽ hình giống 100% ảnh (độ dày 1pt)
                # Tọa độ các điểm
                tikz_code = r'''\begin{center} \begin{tikzpicture}[line width=1pt, scale=0.8]
                \coordinate (B) at (0,0);
                \coordinate (A) at (-1.5,1.2);
                \coordinate (C) at (2.5,1.2);
                \coordinate (B_p) at (0,4.5);
                \coordinate (A_p) at (-1.5,5.7);
                \coordinate (C_p) at (2.5,5.7);
                \draw (A_p) -- (B_p) -- (C_p) -- (A_p);
                \draw (A_p) -- (A);
                \draw (B_p) -- (B);
                \draw (C_p) -- (C);
                \draw (B) -- (C);
                \draw (B_p) -- (C);
                \draw[dashed] (A) -- (C);
                \draw (A) -- (B);
                \node[left] at (A) {$A$};
                \node[below] at (B) {$B$};
                \node[right] at (C) {$C$};
                \node[left] at (A_p) {$A'$};
                \node[above] at (B_p) {$B'$};
                \node[right] at (C_p) {$C'$};
                \end{tikzpicture} \end{center}''' 

                # Nội dung lời giải chi tiết
                loigiai = (r'''Đáy $ABC$ là tam giác vuông cân tại $B$ và $AC = %s \Rightarrow BC = AB = \dfrac{AC}{\sqrt{2}} = \dfrac{%s}{\sqrt{2}} = %s$.\\\\
                             $\Delta BB'C$ vuông tại $B \Rightarrow BB' = \sqrt{\left(B'C\right)^2 - BC^2} = \sqrt{\left(%s\right)^2 - \left(%s\right)^2} = %s$.\\\\
                             $V = \dfrac{1}{3} \cdot BB' \cdot S_{\Delta ABC} = \dfrac{1}{3} \cdot %s \cdot \dfrac{1}{2} \cdot \left(%s\right)^2 = %s$.\\\\
                             Vậy thể tích của khối lăng trụ đứng $ABC.A'B'C'$ là $V = %s$.'''
                           % (latex(val_AC), latex(val_AC), latex(val_BC),
                              latex(n*a), latex(val_BC), latex(val_BB_prime),
                              latex(val_BB_prime), latex(val_BC), latex(val_V), latex(val_V)
                              ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +
                       '\\loigiai{' + tikz_code + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

