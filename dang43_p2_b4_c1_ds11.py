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


def bt_dang43_p2_b4_c1_ds11(self):
        # Khai báo biến
        # Random hệ số a trong cos(ax) = 0 và hệ số khoảng m trong (0; m*pi)
        a = random.choice([2, 3, 4])
        m = random.choice([1, 2])

        # Khai báo biến sympy
        x = symbols('x')
        k = symbols('k', integer=True)

        # Nội dung câu hỏi
        if a == 2:
            noidungcauhoi = (r'Cho phương trình $\cos 2x = 0$.')
        else:
            noidungcauhoi = (r'Cho phương trình $\cos %sx = 0$.' % (a))

        ########################################################################
        # Nhận biết ############################################
        nb_da_d = r'\True $x = %s$ là một nghiệm của phương trình' % (latex(Rational(1, 2 * a) * pi))
        nb_lg_d = r'Thay $x = %s$ vào phương trình ta được $\cos\left(%s \cdot %s\right) = \cos\frac{\pi}{2} = 0$. Do đó $x = %s$ là một nghiệm của phương trình.' % (
            latex(Rational(1, 2 * a) * pi), a, latex(Rational(1, 2 * a) * pi), latex(Rational(1, 2 * a) * pi)
        )

        nb_da_s = r'$x = 0$ là một nghiệm của phương trình'
        nb_lg_s = r'Thay $x = 0$ vào phương trình ta được $\cos 0 = 1 \neq 0$, do đó $x = 0$ không phải là nghiệm của phương trình.'

        pair_nb_d = (nb_da_d, nb_lg_d)
        pair_nb_s = (nb_da_s, nb_lg_s)

        ########################################################################
        # Thông hiểu ############################################
        th_da_d = r'\True Nghiệm của phương trình là $x = \frac{\pi}{%s} + \frac{k\pi}{%s}$, với $k \in \mathbb{Z}$' % (2 * a, a)
        th_lg_d = r'Ta có $\cos %sx = 0 \Leftrightarrow %sx = \frac{\pi}{2} + k\pi \Leftrightarrow x = \frac{\pi}{%s} + \frac{k\pi}{%s}$, với $k \in \mathbb{Z}$.' % (a, a, 2 * a, a)

        th_da_s = r'Nghiệm của phương trình là $x = \frac{\pi}{%s} + k\pi$, với $k \in \mathbb{Z}$' % (a)
        th_lg_s = r'Ta có $\cos %sx = 0 \Leftrightarrow %sx = \frac{\pi}{2} + k\pi \Leftrightarrow x = \frac{\pi}{%s} + \frac{k\pi}{%s}$, với $k \in \mathbb{Z}$. Do đó mệnh đề trên là sai.' % (a, a, 2 * a, a)

        pair_th_d = (th_da_d, th_lg_d)
        pair_th_s = (th_da_s, th_lg_s)

        ########################################################################
        # Vận dụng ############################################
        if a == 2:
            vd_da_d = r'\True Phương trình có cùng tập nghiệm với phương trình $\cos^2 x = \frac{1}{2}$'
            vd_lg_d = r'Ta có $\cos^2 x = \frac{1}{2} \Leftrightarrow \frac{1 + \cos 2x}{2} = \frac{1}{2} \Leftrightarrow \cos 2x = 0$. Do đó hai phương trình có cùng tập nghiệm.'

            vd_da_s = r'Phương trình có cùng tập nghiệm với phương trình $\cos^2 x = 1$'
            vd_lg_s = r'Ta có $\cos^2 x = 1 \Leftrightarrow \sin^2 x = 0 \Leftrightarrow \sin x = 0 \Leftrightarrow x = k\pi$. Trong khi phương trình $\cos 2x = 0 \Leftrightarrow x = \frac{\pi}{4} + \frac{k\pi}{2}$. Do đó hai phương trình không có cùng tập nghiệm.'
        elif a == 3:
            vd_da_d = r'\True Phương trình có cùng tập nghiệm với phương trình $4\cos^3 x - 3\cos x = 0$'
            vd_lg_d = r'Ta có $4\cos^3 x - 3\cos x = 0 \Leftrightarrow \cos 3x = 0$. Do đó hai phương trình có cùng tập nghiệm.'

            vd_da_s = r'Phương trình có cùng tập nghiệm với phương trình $4\cos^3 x - 3\cos x = 1$'
            vd_lg_s = r'Ta có $4\cos^3 x - 3\cos x = 1 \Leftrightarrow \cos 3x = 1 \neq 0$. Do đó hai phương trình không có cùng tập nghiệm.'
        else: # a == 4
            vd_da_d = r'\True Phương trình có cùng tập nghiệm với phương trình $\cos^2 2x = \frac{1}{2}$'
            vd_lg_d = r'Ta có $\cos^2 2x = \frac{1}{2} \Leftrightarrow \frac{1 + \cos 4x}{2} = \frac{1}{2} \Leftrightarrow \cos 4x = 0$. Do đó hai phương trình có cùng tập nghiệm.'

            vd_da_s = r'Phương trình có cùng tập nghiệm với phương trình $\cos^2 2x = 1$'
            vd_lg_s = r'Ta có $\cos^2 2x = 1 \Leftrightarrow \sin 2x = 0 \Leftrightarrow 2x = k\pi \Leftrightarrow x = \frac{k\pi}{2}$. Trong khi phương trình $\cos 4x = 0 \Leftrightarrow x = \frac{\pi}{8} + \frac{k\pi}{4}$. Do đó hai phương trình không có cùng tập nghiệm.'

        pair_vd_d = (vd_da_d, vd_lg_d)
        pair_vd_s = (vd_da_s, vd_lg_s)

        ########################################################################
        # Vận dụng cao ############################################
        N_true = a * m
        N_false = N_true // 2 if N_true // 2 > 0 else N_true + 2

        if m == 1:
            interval_str = r'(0; \pi)'
        else:
            interval_str = r'(0; %s\pi)' % (m)

        vdc_da_d = r'\True Trên $%s$, phương trình có đúng %s nghiệm' % (interval_str, N_true)
        vdc_lg_d = (r'Nghiệm của phương trình là $x = \frac{\pi}{%s} + \frac{k\pi}{%s}$. \\ '
                    r'Vì $x \in %s$ nên $0 < \frac{\pi}{%s} + \frac{k\pi}{%s} < %s\pi \Leftrightarrow -\frac{1}{2} < k < %s - \frac{1}{2} \Leftrightarrow -0,5 < k < %s,5$. \\ '
                    r'Vì $k \in \mathbb{Z}$ nên $k \in \{0; 1; \dots; %s\}$, tổng cộng có %s nghiệm.') % (
            2 * a, a, interval_str, 2 * a, a, m, a * m, a * m - 1, a * m - 1, N_true
        )

        vdc_da_s = r'Trên $%s$, phương trình có đúng %s nghiệm' % (interval_str, N_false)
        vdc_lg_s = (r'Nghiệm của phương trình là $x = \frac{\pi}{%s} + \frac{k\pi}{%s}$. \\ '
                    r'Vì $x \in %s$ nên $0 < \frac{\pi}{%s} + \frac{k\pi}{%s} < %s\pi \Leftrightarrow -0,5 < k < %s,5$. \\ '
                    r'Vì $k \in \mathbb{Z}$ nên $k \in \{0; 1; \dots; %s\}$, phương trình có đúng %s nghiệm, không phải %s nghiệm.') % (
            2 * a, a, interval_str, 2 * a, a, m, a * m - 1, a * m - 1, N_true, N_false
        )

        pair_vdc_d = (vdc_da_d, vdc_lg_d)
        pair_vdc_s = (vdc_da_s, vdc_lg_s)

        # Lặp đến khi số câu đúng thoả mãn từ 1 đến 3 câu
        while True:
            sel_nb = random.choice([pair_nb_d, pair_nb_s])
            sel_th = random.choice([pair_th_d, pair_th_s])
            sel_vd = random.choice([pair_vd_d, pair_vd_s])
            sel_vdc = random.choice([pair_vdc_d, pair_vdc_s])

            answers = [sel_nb[0], sel_th[0], sel_vd[0], sel_vdc[0]]
            true_count = sum(r'\True' in ans for ans in answers)

            if 1 <= true_count <= 3:
                break

        # Tách đáp án và lời giải đã ghép cặp chính xác
        shuffled_answers = [sel_nb[0], sel_th[0], sel_vd[0], sel_vdc[0]]
        shuffled_solutions = [sel_nb[1], sel_th[1], sel_vd[1], sel_vdc[1]]

        # Xuất câu hỏi với đáp án và lời giải đã khớp nhau hoàn toàn
        content = (r'\begin{minipage}{\textwidth} ' + '\n'
                   r'\begin{ex}' + '\n' +
                   str(noidungcauhoi) + '\n'
                   r'\choiceTFn' + '\n'
                   '{' + str(shuffled_answers[0]) + '}\n'
                   '{' + str(shuffled_answers[1]) + '}\n'
                   '{' + str(shuffled_answers[2]) + '}\n'
                   '{' + str(shuffled_answers[3]) + '}\n'
                   r'\loigiai{' + '\n'
                   r'\begin{enumEX}[a)]{1}' + '\n'
                   r'\item ' + str(shuffled_solutions[0]) + '\n'
                   r'\item ' + str(shuffled_solutions[1]) + '\n'
                   r'\item ' + str(shuffled_solutions[2]) + '\n'
                   r'\item ' + str(shuffled_solutions[3]) + '\n'
                   r'\end{enumEX}}' + '\n'
                   r'\end{ex}' + '\n'
                   r'\end{minipage}' + '\n\n')
        return content

