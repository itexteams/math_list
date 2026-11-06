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


def bt_dang10_p2_b3_c1_hh11(self):
    # Khai báo biến và tham số ngẫu nhiên cho bài toán
    # Tỉ lệ IP/IO = 1/2 là cố định trong hình học không gian này, ta random các tỉ số sai để tạo phương án
    ti_so_dung = "1/2"
    ti_so_sai = random.choice(["1/3", "1/4", "2/3", "3/4"])

    # Hình vẽ TikZ vẽ 100% đúng hình ảnh cung cấp: nét 1pt, điểm 1pt, màu black
    hinh_ve = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
        \\coordinate (S) at (2.5, 4.5);
        \\coordinate (A) at (0.2, 1.2);
        \\coordinate (B) at (4.8, 1.2);
        \\coordinate (D) at (1.7, -0.4);
        \\coordinate (C) at (3.3, -0.4);
        \\coordinate (O) at (intersection of A--C and B--D);
        \\coordinate (M) at ($(S)!0.5!(B)$);
        \\coordinate (N) at ($(S)!0.5!(D)$);
        \\coordinate (P) at ($(S)!0.5!(C)$);
        \\coordinate (E) at (intersection of M--N and S--O);
        \\coordinate (I) at (intersection of C--E and O--P);
        \\draw[line width=1pt] (S)--(A) (S)--(D) (S)--(C) (S)--(B) (A)--(D)--(C)--(B) (S)--(N) (S)--(P) (N)--(D) (P)--(C) (M)--(C) (C)--(E) (M)--(P);
        \\draw[line width=1pt] ($(C)!-0.7!(C)+({cos(-18)},{sin(-18)})$) -- ($(C)!1.8!(C)+({cos(-18)},{sin(-18)})$) node[below right] {$x$};
        \\draw[line width=1pt, dashed] (A)--(B) (A)--(C) (B)--(D) (S)--(O) (M)--(N)  (N)--(P) (O)--(P)   (N)--(C);
        \\fill (S) circle (1pt) node[above] {$S$};
        \\fill (A) circle (1pt) node[left] {$A$};
        \\fill (B) circle (1pt) node[right] {$B$};
        \\fill (D) circle (1pt) node[below left] {$D$};
        \\fill (C) circle (1pt) node[below right] {$C$};
        \\fill (O) circle (1pt) node[below] {$O$};
        \\fill (M) circle (1pt) node[left] {$M$};
        \\fill (N) circle (1pt) node[above right] {$N$};
        \\fill (P) circle (1pt) node[right] {$P$};
        \\fill (E) circle (1pt) node[above left] {$E$};
        \\fill (I) circle (1pt) node[below right] {$I$};
    \\end{tikzpicture}
    \\end{center}"""

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang, $AB$ là đáy lớn, $O$ là giao điểm của $AC$ và $BD$. Gọi $M, N$ lần lượt là trung điểm của $SB$ và $SD$.'''
                    )

    ########################################################################
    # Nhận biết (Ý a) ######################################################
    nb_da_1_d = '\\True $CD // (SAB)$'
    nb_da_1_s = '$CD$ cắt mặt phẳng $(SAB)$'
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    list_nb_1 = [nb_da_1]

    loigiai_nb_1 = ('''$CD // AB$ (tính chất hình thang)\\\\
    $CD \\not\\subset (SAB), AB \\subset (SAB)$\\\\
    $\\Rightarrow CD // (SAB)$\\\\
    Vậy mệnh đề đúng.'''
                    )

    list_nb_2 = [loigiai_nb_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu (Ý b) #####################################################
    th_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(CMN)$ và $(ABCD)$ là đường thẳng đi qua $C$ và song song với $BD$'
    th_da_1_s = 'Giao tuyến của hai mặt phẳng $(CMN)$ và $(ABCD)$ là đường thẳng đi qua $C$ và cắt $BD$'
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    list_th_1 = [th_da_1]

    loigiai_th_1 = ('''$C \\in (CMN) \\cap (ABCD)$\\\\
    $MN // BD; MN \\subset (CMN); BD \\subset (ABCD)$ (đường trung bình)\\\\
    $\\Rightarrow (CMN) \\cap (ABCD) = Cx // MN // BD$\\\\
    Vậy mệnh đề đúng.'''
                    )

    list_th_2 = [loigiai_th_1]

    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ########################################################################
    # Vận dụng (Ý c) #######################################################
    vd_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(SAD)$ và $(SBC)$ là đường thẳng đi qua $S$ và cắt hai đường thẳng $AD, BC$'
    vd_da_1_s = 'Giao tuyến của hai mặt phẳng $(SAD)$ và $(SBC)$ là đường thẳng đi qua $S$ và song song với $AD, BC$'
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    list_vd_1 = [vd_da_1]

    loigiai_vd_1 = ('''Xét hai mặt phẳng $(SAD)$ và $(SBC)$ có:\\\\
    Điểm $S$ chung\\\\
    Hình thang $ABCD$ có $AB$ là đáy lớn nên $AD$ cắt $BC$. Gọi $K = AD \\cap BC \\Rightarrow K$ là điểm chung.\\\\
    Giao tuyến của hai mặt phẳng $(SAD)$ và $(SBC)$ là $SK$ (cắt $AD$; cắt $BC$).\\\\
    Vậy mệnh đề sai.'''
                    )

    list_vd_2 = [loigiai_vd_1]

    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ########################################################################
    # Vận dụng cao (Ý d) ###################################################
    vdc_da_1_d = '\\True Gọi $P$ là trung điểm của $SC, I$ là giao điểm của $OP$ và $(CMN)$. Khi đó $\\dfrac{IP}{IO} = \\dfrac{1}{2}$'
    vdc_da_1_s = ('Gọi $P$ là trung điểm của $SC, I$ là giao điểm của $OP$ và $(CMN)$. Khi đó $\\dfrac{IP}{IO} = %s$'
                  % (ti_so_sai.replace("1/3", "\\dfrac{1}{3}").replace("1/4", "\\dfrac{1}{4}").replace("2/3", "\\dfrac{2}{3}").replace("3/4", "\\dfrac{3}{4}")))
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    list_vdc_1 = [vdc_da_1]

    loigiai_vdc_1 = ('''$OP \\subset (SAC)$\\\\
    Trong $(SBD)$, gọi $E$ là giao điểm của $MN$ và $SO$\\\\
    $\\Rightarrow \\begin{cases} E \\in MN, MN \\subset (CMN) \\\\ E \\in SO, SO \\subset (SAC) \\end{cases}$\\\\
    $\\Rightarrow E \\in (CMN) \\cap (SAC)$\\\\
    $\\Rightarrow CE = (CMN) \\cap (SAC)$\\\\
    Trong $(SAC)$ gọi $I$ là giao điểm của $OP$ và $CE$\\\\
    $\\Rightarrow \\begin{cases} I \\in OP \\\\ I \\in CE \\subset (CMN) \\end{cases} \\Rightarrow I = OP \\cap (CMN)$\\\\
    $ME // DO$, $M$ là trung điểm $SD \\Rightarrow E$ là trung điểm $SO$.\\\\
    $P$ là trung điểm $SC \\Rightarrow EP // OC, EP = \\dfrac{1}{2} OC$.\\\\
    $\\Rightarrow \\dfrac{IP}{IO} = \\dfrac{EP}{OC} = \\dfrac{1}{2}$.'''
                    )

    list_vdc_2 = [loigiai_vdc_1]

    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    # Lặp đến khi đáp án có từ 1 đến 3 đúng
    while True:
        nb_da_1 = random.choice(list_nb_da_1)
        th_da_1 = random.choice(list_th_da_1)
        vd_da_1 = random.choice(list_vd_da_1)
        vdc_da_1 = random.choice(list_vdc_da_1)

        answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
        true_count = count_true_answers(answers)

        if 1 <= true_count <= 3:
            break

    # Gán lại vào list
    list_nb_1 = [nb_da_1]
    list_th_1 = [th_da_1]
    list_vd_1 = [vd_da_1]
    list_vdc_1 = [vdc_da_1]

    combined_nb = list(zip(list_nb_1, list_nb_2))
    combined_th = list(zip(list_th_1, list_th_2))
    combined_vd = list(zip(list_vd_1, list_vd_2))
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    random.shuffle(combined_nb)
    random.shuffle(combined_th)
    random.shuffle(combined_vd)
    random.shuffle(combined_vdc)

    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

    # Xuất câu hỏi với hình vẽ được đặt ở đầu phần lời giải
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n'
        '\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n' +
        str(hinh_ve) + '\n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content

