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


def bt_dang6_p2_b1_c2_hh11(self):
            # Khai báo biến
            # B1: Nghiên cứu đề bài và B3: Random số liệu
            # Chọn ngẫu nhiên giá trị a là số nguyên chẵn từ 2 đến 10 để tính toán đẹp
            val_a = random.choice([2, 4, 6, 8, 10])
            a_sym = symbols('a')

            # Tính toán các giá trị cụ thể
            # MD = ND là đường cao tam giác đều cạnh a: a*sqrt(3)/2
            val_md_exact = Rational(val_a, 2) * sqrt(3)
            val_md_wrong = Rational(val_a, 2) * sqrt(2)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tứ diện đều $ABCD$ có cạnh bằng $a = %s$. Gọi $M$ là trung điểm của cạnh $BC$ và $N$ là trung điểm của cạnh $AC$.''' 
                             % (latex(val_a)))

            # B2: Viết lại y hệt bài toán theo mẫu code python
            ########################################################################
            # Nhận biết
            ########################################################################
            nb_da_1_d = '\\True $MN \\parallel AB$'
            nb_da_1_s = '$MN \\perp AB$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Trong tam giác $ABC$, $M$ là trung điểm của $BC$ và $N$ là trung điểm của $AC$. Theo tính chất đường trung bình, ta có $MN \\parallel AB$.''')

            ########################################################################
            # Thông hiểu
            ########################################################################
            th_da_1_d = '\\True $MD = ND = %s$' % (latex(val_md_exact))
            th_da_1_s = '$MD = ND = %s$' % (latex(val_md_wrong))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Vì $ABCD$ là tứ diện đều cạnh $a=%s$ nên các mặt là các tam giác đều. $MD$ và $ND$ lần lượt là các đường cao của tam giác đều $BCD$ và $ACD$. \\\\ 
                            Ta có $MD = ND = \\frac{%s \\sqrt{3}}{2} = %s$.''' 
                            % (latex(val_a), latex(val_a), latex(val_md_exact)))

            ########################################################################
            # Vận dụng
            ########################################################################
            vd_da_1_d = '\\True $(AB, DM) = (MN, DM)$'
            vd_da_1_s = '$(AB, DM) = (BC, DM)$'
            list_vd_1_da = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_1_da)

            loigiai_vd_1 = ('''Vì $MN \\parallel AB$ nên góc giữa hai đường thẳng $AB$ và $DM$ bằng góc giữa hai đường thẳng $MN$ và $DM$. Suy ra $(AB, DM) = (MN, DM)$.''')

            ########################################################################
            # Vận dụng cao
            ########################################################################
            vdc_da_1_d = '\\True $\\cos(AB, DM) = \\frac{\\sqrt{3}}{6}$'
            vdc_da_1_s = '$\\cos(AB, DM) = \\frac{\\sqrt{3}}{3}$'
            list_vdc_1_da = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_1_da)

            loigiai_vdc_1 = ('''Xét tam giác $DMN$ có: $MN = \\frac{AB}{2} = %s$, $MD = ND = %s$. \\\\
                            Áp dụng định lí cosin trong tam giác $DMN$: \\\\
                            $ND^2 = MN^2 + MD^2 - 2MN \\cdot MD \\cdot \\cos \\angle DMN$ \\\\
                            $\\Leftrightarrow %s = %s + %s - 2 \\cdot %s \\cdot %s \\cdot \\cos \\angle DMN$ \\\\
                            $\\Leftrightarrow \\cos \\angle DMN = \\frac{1}{2\\sqrt{3}} = \\frac{\\sqrt{3}}{6}$. \\\\
                            Vì $\\cos \\angle DMN > 0$ nên $\\cos(AB, DM) = \\frac{\\sqrt{3}}{6}$.''' 
                             % (latex(Rational(val_a, 2)), latex(val_md_exact), 
                                latex(val_md_exact**2), latex(Rational(val_a, 2)**2), latex(val_md_exact**2),
                                latex(Rational(val_a, 2)), latex(val_md_exact)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_1_da)
                ans_vdc = random.choice(list_vdc_1_da)
                if 1 <= count_true_answers([ans_nb, ans_th, ans_vd, ans_vdc]) <= 3:
                    break

            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            # Xuất nội dung (Không dùng raw string r'' theo yêu cầu)
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\begin{center} \n'
                '\\begin{tikzpicture}[scale=0.8, font=\\footnotesize, line join=round, line cap=round] \n'
                '\\coordinate (B) at (0,0); \\coordinate (C) at (4,0); \\coordinate (D) at (1.5,-1.5); \\coordinate (A) at (2,4); \n'
                '\\coordinate (M) at ($(B)!0.5!(C)$); \\coordinate (N) at ($(A)!0.5!(C)$); \n'
                '\\draw[dashed] (B) -- (C); \\draw (B) -- (D) -- (C) -- (A) -- (B) (A) -- (D); \n'
                '\\draw  (D) -- (N); \n'
                '\\draw[dashed]  (M) -- (N) (D) -- (M); \n'
                '\\fill (A) node[above] {$A$}; \\fill (B) node[left] {$B$}; \n'
                '\\fill (C) node[right] {$C$}; \\fill (D) node[below] {$D$}; \n'
                '\\fill (M) node[above right] {$M$}; \\fill (N) node[right] {$N$}; \n'
                '\\end{tikzpicture} \n'
                '\\end{center} \n'
                '\\choiceTFn \n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(loigiai_nb_1) + '\n'
                '\\item ' + str(loigiai_th_1) + '\n'
                '\\item ' + str(loigiai_vd_1) + '\n'
                '\\item ' + str(loigiai_vdc_1) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

