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


def bt_dang21_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Random cạnh a là một số nguyên dương chẵn để các trung điểm có tọa độ đẹp (nếu cần)
            a_val = random.choice([2, 4, 6, 8, 10])

            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho tứ diện đều $ABCD$ có cạnh bằng $%s$, $M$ là trung điểm cạnh $BC$, $N$ là trung điểm của $AC$.''' 
                             %(latex(a_val)))

            # Hình vẽ TikZ
            hinh_ve = r'''\begin{center}
            \begin{tikzpicture}[scale=1, font=\footnotesize, line join=round, line cap=round]
                \coordinate (B) at (0,0);
                \coordinate (C) at (1.5,-1);
                \coordinate (D) at (4,0);
                \coordinate (A) at (2,3);
                \coordinate (M) at ($(B)!0.5!(C)$);
                \coordinate (N) at ($(A)!0.5!(C)$);
                \draw[dashed] (B)--(D);
                \draw (A)--(B)--(C)--(D)--(A)--(C) (M)--(N) (N)--(D);
                \draw[dashed] (D)--(M) ;
                \fill (A)  node[above] {$A$};
                \fill (B)  node[left] {$B$};
                \fill (C)  node[below] {$C$};
                \fill (D)  node[right] {$D$};
                \fill (M)  node[below left] {$M$};
                \fill (N)  node[right] {$N$};
            \end{tikzpicture}
            \end{center}'''

            ########################################################################
            # Nhận biết: Kiểm tra tính song song
            ########################################################################
            nb_da_1_d = r'\True $MN // AB$'
            nb_da_1_s = r'$MN // CD$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = ('''Trong tam giác $ABC$, $M$ là trung điểm của $BC$ và $N$ là trung điểm của $AC$. 
                            Theo tính chất đường trung bình của tam giác, ta có $MN // AB$ và $MN = \\frac{1}{2}AB$.''')

            ########################################################################
            # Thông hiểu: Tính độ dài đoạn thẳng
            ########################################################################
            # Giá trị đúng: MD = ND = a*sqrt(3)/2
            val_md = sqrt(3) * a_val / 2
            val_md_latex = latex(val_md)

            th_da_1_d = r'\True $MD = ND = %s$' % (val_md_latex)
            th_da_1_s = r'$MD = ND = %s$' % (latex(sqrt(2) * a_val / 2))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = ('''Vì $ABCD$ là tứ diện đều cạnh $%s$ nên các mặt là các tam giác đều. 
                            $DM$ là đường trung tuyến của tam giác đều $BCD$ nên $DM = \\frac{%s \\sqrt{3}}{2} = %s$. 
                            Tương tự, $DN$ là đường trung tuyến của tam giác đều $ACD$ nên $DN = \\frac{%s \\sqrt{3}}{2} = %s$.'''
                            % (latex(a_val), latex(a_val), val_md_latex, latex(a_val), val_md_latex))

            ########################################################################
            # Vận dụng: Góc giữa hai đường thẳng
            ########################################################################
            vd_da_1_d = r'\True $(AB, DM) = (MN, DM)$'
            vd_da_1_s = r'$(AB, DM) = (BC, DM)$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = ('''Ta có $MN // AB$. Theo định nghĩa góc giữa hai đường thẳng trong không gian, 
                            góc giữa $AB$ và $DM$ bằng góc giữa $MN$ và $DM$ (vì $MN$ và $DM$ cắt nhau tại $M$). 
                            Do đó $(AB, DM) = (MN, DM)$.''')

            ########################################################################
            # Vận dụng cao: Tính cosin góc
            ########################################################################
            # Cosin đúng = sqrt(3)/6
            val_cos = r'\frac{\sqrt{3}}{6}'
            th_da_vdc_s = r'\frac{\sqrt{3}}{3}'

            vdc_da_1_d = r'\True $\cos(AB, DM) = %s$' % (val_cos)
            vdc_da_1_s = r'$\cos(AB, DM) = %s$' % (th_da_vdc_s)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = ('''Xét tam giác $MND$ có: \\\\
                            $MN = \\frac{1}{2}AB = %s$, $MD = %s$, $ND = %s$. \\\\
                            Áp dụng định lý cosin trong tam giác $MND$: \\\\
                            $\\cos \\widehat{DMN} = \\frac{MN^2 + MD^2 - ND^2}{2 \\cdot MN \\cdot MD} = \\frac{\\left(%s\\right)^2 + \\left(%s\\right)^2 - \\left(%s\\right)^2}{2 \\cdot %s \\cdot %s} = \\frac{%s}{%s} = \\frac{\\sqrt{3}}{6}$. \\\\
                            Vì $\\frac{\\sqrt{3}}{6} > 0$ nên góc giữa $MN$ và $DM$ là góc $\\widehat{DMN}$. \\\\
                            Vậy $\\cos(AB, DM) = \\cos(MN, DM) = \\frac{\\sqrt{3}}{6}$.'''
                            % (latex(Rational(a_val, 2)), val_md_latex, val_md_latex,
                               latex(Rational(a_val, 2)), val_md_latex, val_md_latex,
                               latex(Rational(a_val, 2)), val_md_latex,
                               latex(Rational(a_val**2, 4)), latex(a_val * sqrt(3) * a_val / 2)))

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                d1 = random.choice(list_nb_da_1)
                d2 = random.choice(list_th_da_1)
                d3 = random.choice(list_vd_da_1)
                d4 = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([d1, d2, d3, d4]) <= 3:
                    shuffled_answers = [d1, d2, d3, d4]
                    shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]
                    break

            # Xuất nội dung
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                str(hinh_ve) + 
                '\\choiceTFn \n'
                '{' + str(shuffled_answers[0]) + '}\n'
                '{' + str(shuffled_answers[1]) + '}\n'
                '{' + str(shuffled_answers[2]) + '}\n'
                '{' + str(shuffled_answers[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(shuffled_solutions[0]) + '\n'
                '\\item ' + str(shuffled_solutions[1]) + '\n'
                '\\item ' + str(shuffled_solutions[2]) + '\n'
                '\\item ' + str(shuffled_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

