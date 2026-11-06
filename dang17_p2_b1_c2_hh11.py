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


def bt_dang17_p2_b1_c2_hh11(self):
            # Khai báo biến
            # Random cạnh a là một số nguyên dương chẵn để các phép tính trung điểm gọn đẹp
            val_a = random.choice([2, 4, 6, 8, 10, 12])
            a_sq = val_a**2

            # TikZ vẽ hình chóp S.ABCD có tất cả các cạnh bằng nhau
            tikz_code = r"""\begin{center}
            \begin{tikzpicture}[scale=0.7, font=\footnotesize, line join=round, line cap=round]
                \coordinate (A) at (0,0);
                \coordinate (B) at (1.5,-1.2);
                \coordinate (C) at (4.5,-1.2);
                \coordinate (D) at (3,0);
                \coordinate (S) at (2.25,3.5);
                \coordinate (I) at ($(S)!0.5!(C)$);
                \coordinate (J) at ($(B)!0.5!(C)$);
                \coordinate (G) at ($(S)!0.666!(J)$);
                \draw (S)--(A)--(B)--(C)--(S)--(B);
                \draw (I)--(J);
                \draw[dashed] (S)--(D)--(A) (D)--(C) (B)--(I) (D)--(G);
                \foreach \p/\pos in {S/above, A/left, B/below left, C/below right, D/right, I/right, J/below, G/below}
                    \fill (\p) circle (1pt) node[\pos] {$\p$};
            \end{tikzpicture}
            \end{center}"""

            # Nội dung câu hỏi
            noidungcauhoi = (r'''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình vuông, tất cả các cạnh của hình chóp đều bằng $%s$. Gọi $I$ và $J$ lần lượt là trung điểm của $SC$ và $BC$. Gọi $G$ là trọng tâm $\triangle SBC$.
            %s''' % (val_a, tikz_code))

            # ================= NHẬN BIẾT: Góc giữa IJ và SA =================
            nb_da_1_d = r'\True Góc giữa $IJ$ và $SA$ bằng $60^\circ$'
            nb_da_1_s = r'Góc giữa $IJ$ và $SA$ bằng $90^\circ$'
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            loigiai_nb_1 = (r'''Vì $I, J$ là trung điểm $SC, BC$ nên $IJ \parallel SB$. Khi đó $(IJ, SA) = (SB, SA) = \widehat{ASB}$. Do $\triangle SAB$ đều nên $\widehat{ASB} = 60^\circ$.''')

            # ================= THÔNG HIỂU: Góc giữa IJ và CD =================
            th_da_1_d = r'\True Góc giữa $IJ$ với $CD$ bằng $60^\circ$'
            th_da_1_s = r'Góc giữa $IJ$ với $CD$ bằng $45^\circ$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            loigiai_th_1 = (r'''Ta có $IJ \parallel SB$ và $CD \parallel AB$. Suy ra $(IJ, CD) = (SB, AB) = \widehat{SBA} = 60^\circ$ (do $\triangle SAB$ đều).''')

            # ================= VẬN DỤNG: Cosin giữa BI và SA =================
            # Kết quả: sqrt(3)/3
            vd_da_1_d = r'\True Cô-sin của góc giữa $BI$ với $SA$ bằng $\frac{\sqrt{3}}{3}$'
            vd_da_1_s = r'Cô-sin của góc giữa $BI$ với $SA$ bằng $\frac{1}{2}$'
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            loigiai_vd_1 = (r'''Sử dụng tích vô hướng: $\vec{BI} \cdot \vec{SA} = (\vec{SI} - \vec{SB}) \cdot \vec{SA} = \frac{1}{2}\vec{SC} \cdot \vec{SA} - \vec{SB} \cdot \vec{SA}$. \\
            Do $\triangle SAC$ vuông tại $S$ nên $\vec{SC} \cdot \vec{SA} = 0$. \\
            $\vec{SB} \cdot \vec{SA} = %s \cdot %s \cdot \cos 60^\circ = %s$. \\
            Suy ra $|\vec{BI} \cdot \vec{SA}| = %s$. Độ dài $BI = \frac{%s\sqrt{3}}{2}$. \\
            $\cos(BI, SA) = \frac{%s}{\frac{%s\sqrt{3}}{2} \cdot %s} = \frac{\sqrt{3}}{3}$.''' 
            % (val_a, val_a, a_sq//2, a_sq//2, val_a, a_sq//2, val_a, val_a))

            # ================= VẬN DỤNG CAO: Cosin giữa DG và SB =================
            # Kết quả: 1/2
            vdc_da_1_d = r'\True Cô-sin của góc giữa $DG$ và $SB$ bằng $\frac{1}{2}$'
            vdc_da_1_s = r'Cô-sin của góc giữa $DG$ và $SB$ bằng $\frac{\sqrt{3}}{6}$'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            loigiai_vdc_1 = (r'''Ta có $\vec{DG} = \frac{1}{3}\vec{SB} + \frac{1}{3}\vec{SC} - \vec{SD}$. \\
            Tính $\vec{DG} \cdot \vec{SB} = \frac{1}{3}SB^2 + \frac{1}{3}\vec{SC}\cdot\vec{SB} - \vec{SD}\cdot\vec{SB} = \frac{1}{3}%s + \frac{1}{3}\frac{%s}{2} - 0 = \frac{%s}{2}$. \\
            Độ dài $DG = %s$. Vậy $\cos(DG, SB) = \frac{%s/2}{%s \cdot %s} = \frac{1}{2}$.''' 
            % (a_sq, a_sq, a_sq, val_a, a_sq, val_a, val_a))

            # ================= VÒNG LẶP RANDOM ĐÁP ÁN (1-3 câu đúng) =================
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lời giải tương ứng
            list_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            # ================= XUẤT NỘI DUNG =================
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' + 
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(nb_da_1) + '}\n'
                '{' + str(th_da_1) + '}\n'
                '{' + str(vd_da_1) + '}\n'
                '{' + str(vdc_da_1) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(list_solutions[0]) + '\n'
                '\\item ' + str(list_solutions[1]) + '\n'
                '\\item ' + str(list_solutions[2]) + '\n'
                '\\item ' + str(list_solutions[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n\\end{minipage}\n')
            return content

