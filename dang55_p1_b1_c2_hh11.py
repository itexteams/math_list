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


def bt_dang55_p1_b1_c2_hh11(self):
            # Khai báo biến
            # Khai báo biến
            lisdang=['1']
            dang = random.choice(lisdang)

            if dang == '1':
                # Bước 1: Random độ dài cạnh a (chọn số chẵn để trung điểm là số nguyên)
                a = randint(1, 5) * 2


                cm_val = Rational(a, 2)
                ac_val = a * sqrt(2)
                c_prime_m_val = (a * sqrt(5)) / 2
                a_prime_m_val = Rational(3 * a, 2)

                # Kết quả cosin (không đổi theo a): sqrt(10)/10
                kq_chuan = sqrt(10)/10
                da = '$%s$' % (latex(kq_chuan))

                # Các đáp án nhiễu
                s = [
                    '$0$',
                    '$\\frac{\\sqrt{2}}{2}$',
                    '$\\frac{1}{2}$',
                    '$\\frac{\\sqrt{5}}{5}$',
                    '$\\frac{3}{10}$',
                    '$\\frac{\\sqrt{3}}{2}$'
                ]
                if da in s: s.remove(da)
                random.shuffle(s)
                das1, das2, das3 = s[0], s[1], s[2]

                # Câu hỏi
                noidungcauhoi = ('''Cho hình lập phương $ABCD.A'B'C'D'$ có cạnh bằng $%s$. Gọi $M$ là trung điểm của cạnh $CD$. Tính cosin của góc giữa hai đường thẳng $AC$ và $C'M$.'''
                                % (latex(a)))

                # Các đáp án
                da_d = ('\\True ' + str(da))
                list_1 = [da_d, str(das1), str(das2), str(das3)]
                random.shuffle(list_1)

                # Hình vẽ TikZ
                hinh_ve = ('''\\begin{center}
            \\begin{tikzpicture}[scale=2, line join=round, line cap=round, >=stealth]
                \\coordinate (A) at (0.5,1.5);
                \\coordinate (B) at (0,1);
                \\coordinate (C) at (1.2,1);
                \\coordinate (D) at (1.7,1.5);
                \\coordinate (A1) at (0.5,0.5);
                \\coordinate (B1) at (0,0);
                \\coordinate (C1) at (1.2,0);
                \\coordinate (D1) at (1.7,0.5);
                \\coordinate (M) at ($(C)!0.5!(D)$);
                \\draw[dashed] (A)--(A1)  (A1)--(B1) (A1)--(D1) (A1)--(C1) (A1)--(M);
                \\draw (B)--(C)--(D)--(D1)--(C1)--(B1)--cycle;
                \\draw (C)--(C1) (A)--(B) (A)--(D);
                \\draw (A)--(C);
                \\draw (C1)--(M); 
                \\draw[fill=black] (A)  node[above] {$A$};
                \\draw[fill=black] (B)  node[left] {$B$};
                \\draw[fill=black] (C)  node[below right] {$C$};
                \\draw[fill=black] (D)  node[right] {$D$};
                \\draw[fill=black] (A1)  node[left] {$A'$};
                \\draw[fill=black] (B1)  node[below] {$B'$};
                \\draw[fill=black] (C1)  node[below] {$C'$};
                \\draw[fill=black] (D1)  node[right] {$D'$};
                \\draw[fill=black] (M)  node[above left] {$M$};
            \\end{tikzpicture}
            \\end{center}''')

                # Lời giải chi tiết theo tham số a
                loigiai = ('''Ta có $AC \\parallel A'C'$ nên góc giữa $AC$ và $C'M$ cũng bằng góc giữa $A'C'$ và $C'M$, là góc $\\widehat{A'C'M}$.\\\\
                Với cạnh hình lập phương bằng $%s$, ta có:\\\\
                - $A'C' = %s\\sqrt{2}$ (đường chéo của hình vuông $A'B'C'D'$).\\\\
                - Trong tam giác vuông $CC'M$ có $CM = \\frac{%s}{2} = %s$, $CC' = %s$.\\\\
                Suy ra $C'M = \\sqrt{CC'^2 + CM^2} = \\sqrt{%s^2 + %s^2} = \\sqrt{%s} = %s$.\\\\
                - Trong tam giác vuông $A'DM$ có $A'D = %s\\sqrt{2}$ (đường chéo mặt bên) và $DM = %s$.\\\\
                Suy ra $A'M = \\sqrt{A'D^2 + DM^2} = \\sqrt{(%s\\sqrt{2})^2 + %s^2} = \\sqrt{%s + %s} = \\sqrt{%s} = %s$.\\\\
                Xét tam giác $A'MC'$, áp dụng hệ quả định lý cosin ta có:\\\\
                $\\cos \\widehat{A'C'M} = \\frac{A'C'^2 + C'M^2 - A'M^2}{2 \\cdot A'C' \\cdot C'M} = \\frac{(%s\\sqrt{2})^2 + (%s)^2 - (%s)^2}{2 \\cdot %s\\sqrt{2} \\cdot %s}$\\\\
                $= \\frac{%s + %s - %s}{%s\\sqrt{10}} = \\frac{%s}{%s\\sqrt{10}} = \\frac{1}{\\sqrt{10}} = \\frac{\\sqrt{10}}{10}$.\\\\
                Vậy cosin của góc cần tìm là $\\frac{\\sqrt{10}}{10}$.'''
                % (latex(a), latex(a), 
                   latex(a), latex(cm_val), latex(a), 
                   latex(a), latex(cm_val), latex(a**2 + cm_val**2), latex(c_prime_m_val),
                   latex(a), latex(cm_val),
                   latex(a), latex(cm_val), latex(2*a**2), latex(cm_val**2), latex(2*a**2 + cm_val**2), latex(a_prime_m_val),
                   latex(a), latex(c_prime_m_val), latex(a_prime_m_val), latex(a), latex(c_prime_m_val),
                   latex(2*a**2), latex(a**2 + cm_val**2), latex(a_prime_m_val**2), latex(a**2 * 5),
                   latex(a**2), latex(a**2)
                  ))

            # Xuất câu trắc nghiệm
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + str(noidungcauhoi) +  '\n'
                '\\choice \n'
                '{' + str(list_1[0]) + '}\n'
                '{' + str(list_1[1]) + '}\n'
                '{' + str(list_1[2]) + '}\n'
                '{' + str(list_1[3]) + '}\n'
                '\\loigiai{' +hinh_ve + str(loigiai) + '}\n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

