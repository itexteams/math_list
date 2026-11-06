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


def bt_dang26_p3_b6_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến sympy
            a = symbols('a')

            # Danh sách dạng (để mở rộng sau này)
            lisdang = ['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Random hệ số của AC = m*a*sqrt(2) và B'C = n*a
                m = random.randint(1, 3)
                n = random.randint(m + 2, m + 5) 

                # Tính toán các thông số
                val_AC = m * sqrt(2) 
                val_BC = m 

                # BB' = sqrt(B'C^2 - BC^2)
                h_sq = n**2 - m**2
                val_BB_prime = sqrt(h_sq) 

                # Diện tích đáy S = 1/2 * BC^2
                val_S = Rational(1, 2) * (m**2)

                # Thể tích V = 1/3 * BB' * S (Giữ nguyên logic 1/3 của code gốc)
                val_V = simplify(Rational(1, 3) * val_BB_prime * val_S)

                # --- PHẦN XỬ LÝ SỐ THẬP PHÂN ---
                # Tính toán giá trị số (thế a = 1 để lấy hệ số)
                val_V_numeric = float(val_V.subs(a, 1).evalf())
                # Làm tròn đến hàng phần chục (1 chữ số sau dấu phẩy)
                val_V_rounded = round(val_V_numeric, 1)
                # Chuyển dấu chấm thành dấu phẩy theo chuẩn VN
                str_V_decimal = str(val_V_rounded).replace('.', ',')

                # Đáp án đúng dạng số thập phân
                da = '$V \\approx %s a^3$' % str_V_decimal
                kqz = str_V_decimal # Gán giá trị cho kqz để dùng ở biến dapan

                # Tạo các đáp án sai (dạng số thập phân)
                s = [
                    '$V \\approx %s a^3$' % str(round(val_V_numeric * 1.5, 1)).replace('.', ','),
                    '$V \\approx %s a^3$' % str(round(val_V_numeric * 0.7, 1)).replace('.', ','),
                    '$V \\approx %s a^3$' % str(round(val_V_numeric + 2.1, 1)).replace('.', ','),
                    '$V \\approx %s a^3$' % str(round(val_V_numeric * 2.2, 1)).replace('.', ','),
                    '$V \\approx %s a^3$' % str(round(val_V_numeric * 0.5, 1)).replace('.', ','),
                ]

                random.shuffle(s)
                das1, das2, das3 = s[:3]

                # Câu hỏi
                noidungcauhoi = ('''Cho khối lăng trụ đứng $ABC.A'B'C'$ có $B'C = %s$, đáy $ABC$ là tam giác vuông cân tại $B$ và $AC = %s$. Thể tích $V$ của khối lăng trụ đứng $ABC.A'B'C'$ bằng bao nhiêu? (làm tròn kết quả đến hàng phần chục).'''
                                 % (latex(n*a), latex(val_AC)))

                # Các đáp án cho vào list
                da_d = '\\True ' + str(da)
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # TikZ code
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
                loigiai = (r'''Đáy $ABC$ là tam giác vuông cân tại $B$ và $AC = %s \Rightarrow BC = AB = \dfrac{AC}{\sqrt{2}} = %s$.\\\\
                             $\Delta BB'C$ vuông tại $B \Rightarrow BB' = \sqrt{\left(B'C\right)^2 - BC^2} = \sqrt{\left(%s\right)^2 - \left(%s\right)^2} = %s$.\\\\
                             $V = \dfrac{1}{3} \cdot BB' \cdot S_{\Delta ABC} = \dfrac{1}{3} \cdot %s \cdot \dfrac{1}{2} \cdot \left(%s\right)^2 = %s \approx %s$.\\\\
                             Vậy thể tích của khối lăng trụ đứng $ABC.A'B'C'$ xấp xỉ $%s$.'''
                           % (latex(val_AC), latex(val_BC),
                              latex(n*a), latex(val_BC), latex(val_BB_prime),
                              latex(val_BB_prime), latex(val_BC), latex(val_V), str_V_decimal, str_V_decimal
                              ))

                dapan = '\\shortans[0]{$%s$}\n' % str_V_decimal
            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                       '\\begin{ex}\n' + str(noidungcauhoi) + '\n' +str(dapan)+
                       '\\loigiai{' + tikz_code + str(loigiai) + '}\n'
                       '\\end{ex}\n \\end{minipage} \n\n')
            return content

