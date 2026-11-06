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


def bt_dang8_p2_b2_c1_hh11(self):
    # Khai báo và random tỉ số đáy AD = k * BC (k = 2 hoặc 3)
    k_val = random.choice([2, 3])
    if k_val == 2:
        ti_so_day_str = "AD = 2BC"
        he_so_MN_EF = Rational(2, 3)
        ti_so_dien_tich_dung = Rational(4, 9)
        ti_so_dien_tich_sai = Rational(2, 3)
        loi_giai_ti_so_diem = "B, C \\text{ lần lượt là trung điểm của } KA \\text{ và } KD"
    else:
        ti_so_day_str = "AD = 3BC"
        he_so_MN_EF = Rational(1, 2)
        ti_so_dien_tich_dung = Rational(1, 4)
        ti_so_dien_tich_sai = Rational(1, 2)
        loi_giai_ti_so_diem = "\\dfrac{KB}{KA} = \\dfrac{KC}{KD} = \\dfrac{1}{3}"

    # Hình vẽ TikZ chuẩn
    hinh_ve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (S) at (0,4.2);
    \\coordinate (A) at (-2,-0.5);
    \\coordinate (D) at (3.2,-0.5);
    \\coordinate (B) at (-1.3,-1.9);
    \\coordinate (C) at (1.5,-1.9);
    \\coordinate (K) at (-0.6,-3.3);
    \\coordinate (E) at ($(S)!0.5!(A)$);
    \\coordinate (F) at ($(S)!0.5!(D)$);
    \\coordinate (M) at (intersection of K--E and S--B);
    \\coordinate (N) at (intersection of K--F and S--C);
    \\coordinate (I) at (intersection of A--M and S--K);
    \\draw[line width=1pt] (S)--(A) (S)--(D) (A)--(B)--(K)--(C)--(D);
    \\draw[line width=1pt] (S)--(K) (S)--(M) (S)--(N) (E)--(M) (F)--(N) (K)--(M) (K)--(N);
    \\draw[line width=1pt] (A)--(I) (D)--(I);
    \\draw[line width=1pt, dashed] (A)--(D) (B)--(C) (E)--(F);
    \\draw[line width=1pt, dashed] (E)--(C) (F)--(B);
    \\draw[line width=1pt, dashed] (M)--(N);
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below right] {$C$};
    \\fill (K) circle (1pt) node[below] {$K$};
    \\fill (E) circle (1pt) node[above left] {$E$};
    \\fill (F) circle (1pt) node[above right] {$F$};
    \\fill (M) circle (1pt) node[left] {$M$};
    \\fill (N) circle (1pt) node[right] {$N$};
    \\fill (I) circle (1pt) node[below right] {$I$};
    \\end{tikzpicture}
    \\end{center}''')

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình thang ($AD$ là đáy lớn, $BC$ là đáy nhỏ). Gọi $E, F$ lần lượt là trung điểm của $SA$ và $SD$. $K$ là giao điểm của các đường thẳng $AB$ và $CD$. Khi đó:''')

    ########################################################################
    # a) Nhận biết: Giao điểm M của SB và (CDE)
    ########################################################################
    nb_da_d = '\\True Giao điểm $M$ của đường thẳng $SB$ và mặt phẳng $(CDE)$ là điểm thuộc đường thẳng $KE$'
    nb_lg_d = ('''Trong mp $(ABCD)$, gọi $K = AB \\cap CD$. Khi đó $K \\in CD \\subset (CDE)$ nên $KE \\subset (CDE)$. \\\\
    Trong mp $(SAB)$, gọi $M = KE \\cap SB$. Vì $KE \\subset (CDE)$ nên $M = SB \\cap (CDE)$. \\\\
    Vậy giao điểm $M$ của $SB$ và $(CDE)$ thuộc đường thẳng $KE$.''')

    nb_da_s = 'Giao điểm $M$ của đường thẳng $SB$ và mặt phẳng $(CDE)$ là điểm thuộc đường thẳng $KF$'
    nb_lg_s = ('''Ta có $M$ là giao điểm của $SB$ với $(CDE)$, mà $SB, SA, AB$ cùng thuộc mặt phẳng $(SAB)$ chứa điểm $K = AB \\cap CD$ và $E \\in SA$. \\\\
    Do đó $M = SB \\cap KE$, tức $M$ thuộc đường thẳng $KE$ chứ không thuộc $KF$. Mệnh đề sai.''')

    pairs_nb = [(nb_da_d, nb_lg_d), (nb_da_s, nb_lg_s)]

    ########################################################################
    # b) Thông hiểu: SC cắt (EFM) tại N và hình dạng tứ giác EFNM
    ########################################################################
    th_da_d = '\\True Đường thẳng $SC$ cắt mặt phẳng $(EFM)$ tại $N$. Tứ giác $EFNM$ là hình thang'
    th_lg_d = ('''Mặt phẳng $(EFM)$ chính là mặt phẳng $(EFK)$. \\\\
    Trong mp $(SCD)$, gọi $N = KF \\cap SC$. Do $KF \\subset (EFK)$ nên $SC \\cap (EFM) = N$. \\\\
    Ta có: $\\begin{cases} MN = (EFK) \\cap (SBC) \\\\ EF // BC \\\\ EF \\subset (EFK), \\ BC \\subset (SBC) \\end{cases} \\Rightarrow MN // EF // BC$. \\\\
    Vì $EF // MN$ và $MN \\ne EF$ nên tứ giác $EFNM$ là hình thang.''')

    th_da_s = 'Đường thẳng $SC$ cắt mặt phẳng $(EFM)$ tại $N$. Tứ giác $EFNM$ là hình bình hành'
    th_lg_s = ('''Mặt phẳng $(EFM)$ chính là $(EFK)$. Trong mp $(SCD)$, gọi $N = KF \\cap SC \\Rightarrow SC \\cap (EFM) = N$. \\\\
    Hai mặt phẳng $(EFK)$ và $(SBC)$ chứa hai đường thẳng song song $EF // BC$ nên giao tuyến $MN // EF$. \\\\
    Do $E, F$ là trung điểm của $SA, SD$ nên $EF = \\dfrac{1}{2}AD$. Mặt khác qua phép chiếu/định lí Ta-lét ta có $MN \\ne EF$, do đó tứ giác $EFNM$ chỉ là hình thang, không phải hình bình hành. Mệnh đề sai.''')

    pairs_th = [(th_da_d, th_lg_d), (th_da_s, th_lg_s)]

    ########################################################################
    # c) Vận dụng: Sự đồng quy của AM, DN, SK
    ########################################################################
    vd_da_d = '\\True Các đường thẳng $AM, DN, SK$ cùng đi qua một điểm'
    vd_lg_d = ('''Xét ba mặt phẳng đôi một cắt nhau $(SAB), (SCD)$ và $(EFK)$: \\\\
    $\\bullet$ $(SAB) \\cap (SCD) = SK$. \\\\
    $\\bullet$ $(SAB) \\cap (EFK) = KE$ (chứa đoạn $AM$ kéo dài). Trong mp $(SAB)$, đường thẳng $AM$ cắt $SK$ tại điểm $I$. \\\\
    $\\bullet$ Do $I \\in SK \\subset (SCD)$ và $I \\in (EFK)$, nên $I$ phải thuộc giao tuyến của $(SCD)$ và $(EFK)$, tức là $I \\in KF$. \\\\
    Trong mp $(SCD)$, vì $N = KF \\cap SC$ nên $I, N, D$ thẳng hàng, suy ra $DN$ cũng đi qua $I$. \\\\
    Vậy ba đường thẳng $AM, DN, SK$ đồng quy tại điểm $I$.''')

    vd_da_s = 'Các đường thẳng $AM, DN, SK$ đôi một song song với nhau'
    vd_lg_s = ('''Trong mp $(SAB)$, đường thẳng $AM$ và $SK$ cắt nhau tại điểm $I$ (do $A, B, S, K$ cùng thuộc $(SAB)$ và $AM$ không song song với $SK$). \\\\
    Do đó ba đường thẳng này đồng quy tại $I$, không thể đôi một song song. Mệnh đề sai.''')

    pairs_vd = [(vd_da_d, vd_lg_d), (vd_da_s, vd_lg_s)]

    ########################################################################
    # d) Vận dụng cao: Tỉ số diện tích KMN và KEF
    ########################################################################
    vdc_da_d = ('\\True Cho biết $%s$. Tỉ số diện tích của hai tam giác $KMN$ và $KEF$ bằng $\\dfrac{S_{\\Delta KMN}}{S_{\\Delta KEF}} = %s$'
                % (ti_so_day_str, latex(ti_so_dien_tich_dung)))
    vdc_lg_d = ('''Khi $%s$, áp dụng định lí Ta-lét trong tam giác $KAD$ có $BC // AD$, ta có $%s$. \\\\
    Áp dụng định lý Menelaus cho tam giác $SAK$ với cát tuyến $EMB$: \\\\
    $\\dfrac{ES}{EA} \\cdot \\dfrac{BA}{BK} \\cdot \\dfrac{MK}{MS} = 1 \\Rightarrow 1 \\cdot \\dfrac{KA-KB}{BK} \\cdot \\dfrac{MK}{MS} = 1 \\Rightarrow \\dfrac{KM}{KE} = \\dfrac{KN}{KF} = %s$. \\\\
    Vì $\\Delta KMN \\backsim \\Delta KEF$ theo tỉ số đồng dạng $k_0 = %s$ nên tỉ số diện tích là: \\\\
    $\\dfrac{S_{\\Delta KMN}}{S_{\\Delta KEF}} = k_0^2 = \\left(%s\\right)^2 = %s$.'''
                % (ti_so_day_str, loi_giai_ti_so_diem, latex(he_so_MN_EF),
                   latex(he_so_MN_EF), latex(he_so_MN_EF), latex(ti_so_dien_tich_dung)))

    vdc_da_s = ('Cho biết $%s$. Tỉ số diện tích của hai tam giác $KMN$ và $KEF$ bằng $\\dfrac{S_{\\Delta KMN}}{S_{\\Delta KEF}} = %s$'
                % (ti_so_day_str, latex(ti_so_dien_tich_sai)))
    vdc_lg_s = ('''Tỉ số đồng dạng giữa hai tam giác đồng dạng $KMN$ và $KEF$ là $k_0 = \\dfrac{KM}{KE} = %s$. \\\\
    Do đó tỉ số diện tích phải bằng bình phương tỉ số đồng dạng: \\\\
    $\\dfrac{S_{\\Delta KMN}}{S_{\\Delta KEF}} = k_0^2 = \\left(%s\\right)^2 = %s \\ne %s$. Mệnh đề sai.'''
                % (latex(he_so_MN_EF), latex(he_so_MN_EF), latex(ti_so_dien_tich_dung), latex(ti_so_dien_tich_sai)))

    pairs_vdc = [(vdc_da_d, vdc_lg_d), (vdc_da_s, vdc_lg_s)]

    # Lặp random đảm bảo số lượng câu đúng từ 1 đến 3
    while True:
        choice_nb = random.choice(pairs_nb)
        choice_th = random.choice(pairs_th)
        choice_vd = random.choice(pairs_vd)
        choice_vdc = random.choice(pairs_vdc)

        answers = [choice_nb[0], choice_th[0], choice_vd[0], choice_vdc[0]]
        true_count = sum('\\True' in ans for ans in answers)

        if 1 <= true_count <= 3:
            break

    # Đóng gói đáp án và lời giải tương ứng
    selected_pairs = [choice_nb, choice_th, choice_vd, choice_vdc]
    shuffled_answers = [p[0] for p in selected_pairs]
    shuffled_solutions = [p[1] for p in selected_pairs]

    # Xuất câu hỏi trắc nghiệm đúng/sai theo chuẩn LaTeX
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' +
        str(noidungcauhoi) + '\n' +
        '\\choiceTF \n'
        '{' + str(shuffled_answers[0]) + '}\n'
        '{' + str(shuffled_answers[1]) + '}\n'
        '{' + str(shuffled_answers[2]) + '}\n'
        '{' + str(shuffled_answers[3]) + '}\n'
        '\\loigiai{ \n' +
        str(hinh_ve) + '\n'
        '\\begin{itemchoice} \n'
        '\\itemch ' + str(shuffled_solutions[0]) + '\n'
        '\\itemch ' + str(shuffled_solutions[1]) + '\n'
        '\\itemch ' + str(shuffled_solutions[2]) + '\n'
        '\\itemch ' + str(shuffled_solutions[3]) + '\n'
        '\\end{itemchoice}} \n'
        '\\end{ex}\n \\end{minipage}\n\n')
    return content

