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


def bt_dang30_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ tứ diện đều ABCD có M, N là trung điểm BC, AC và điểm P trên BD, chuẩn 100% như ảnh[cite: 20]
    # Chú ý: Không dùng ký hiệu % comment bên trong string để tránh lỗi format string[cite: 20]
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,2.6);
    \\coordinate (B) at (-1.8,-0.5);
    \\coordinate (C) at (-0.3,-1.5);
    \\coordinate (D) at (2.4,-0.8);
    \\coordinate (M) at ($(B)!0.5!(C)$);
    \\coordinate (N) at ($(A)!0.5!(C)$);
    \\coordinate (P) at ($(B)!0.4!(D)$);
    \\draw[line width=1pt] (A)--(B)--(C)--(D)--(A)--(C);
    \\draw[line width=1pt] (N)--(M);
    \\draw[line width=1pt, dashed] (B)--(D) (M)--(D) (M)--(P)--(N);
    \\fill (A) circle (1pt) node[above] {$A$};
    \\fill (B) circle (1pt) node[left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[right] {$D$};
    \\fill (M) circle (1pt) node[below left] {$M$};
    \\fill (N) circle (1pt) node[above left] {$N$};
    \\fill (P) circle (1pt) node[above right] {$P$};
    \\end{tikzpicture}
    \\end{center}"""
    
    noidungcauhoi = (
        """Cho tứ diện đều $ABCD$. Gọi $M, N$ là trung điểm của $BC$ và $AC$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Góc giữa hai véc tơ \vec{BA} và \vec{MD} là góc \widehat{NMD}[cite: 20]
    nb_da_1_d = "\\True Góc giữa hai vectơ $\\vec{BA}$ và $\\vec{MD}$ là góc $\\widehat{NMD}$"
    nb_da_1_s = "Góc giữa hai vectơ $\\vec{BA}$ và $\\vec{MD}$ là góc $\\widehat{BMD}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Xét tam giác $ABC$, vì $M$ và $N$ lần lượt là trung điểm của $BC$ và $AC$ nên $MN$ là đường trung bình của tam giác $ABC$. \\\\ Suy ra $MN // AB$ và vectơ $\\vec{MN}$ cùng hướng với vectơ $\\vec{BA}$ (tức là $\\vec{MN} = \\frac{1}{2}\\vec{BA}$). \\\\ Khi đó góc giữa hai vectơ $\\vec{BA}$ và $\\vec{MD}$ được xác định là: \\\\ $(\\vec{BA}, \\vec{MD}) = (\\vec{MN}, \\vec{MD}) = \\widehat{NMD}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: cos(\vec{AB}, \vec{DM}) = \sqrt{3}/6[cite: 20]
    th_da_1_d = "\\True $\\cos(\\vec{AB}, \\vec{DM}) = \\frac{\\sqrt{3}}{6}$"
    th_da_1_s = "$\\cos(\\vec{AB}, \\vec{DM}) = \\frac{\\sqrt{3}}{3}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Giả sử tứ diện đều $ABCD$ có cạnh bằng $a$. Khi đó $AB = a$. \\\\ Tam giác $BCD$ là tam giác đều cạnh $a$, $DM$ là đường trung tuyến đồng thời là đường cao nên $DM = \\frac{a\\sqrt{3}}{2}$. \\\\ Ta phân tích vectơ $\\vec{DM}$ qua đỉnh $B$: \\\\ $\\vec{DM} = \\vec{BM} - \\vec{BD} = \\frac{1}{2}\\vec{BC} - \\vec{BD}$. \\\\ Tích vô hướng của hai vectơ $\\vec{AB}$ và $\\vec{DM}$ là: \\\\ $\\vec{AB} \\cdot \\vec{DM} = \\vec{AB} \\cdot \\left(\\frac{1}{2}\\vec{BC} - \\vec{BD}\\right) = \\frac{1}{2}\\vec{AB} \\cdot \\vec{BC} - \\vec{AB} \\cdot \\vec{BD}$ \\\\ $= -\\frac{1}{2}\\vec{BA} \\cdot \\vec{BC} + \\vec{BA} \\cdot \\vec{BD}$ \\\\ $= -\\frac{1}{2}\\left(a \\cdot a \\cdot \\cos 60^\\circ\\right) + \\left(a \\cdot a \\cdot \\cos 60^\\circ\\right) = -\\frac{a^2}{4} + \\frac{a^2}{2} = \\frac{a^2}{4}$. \\\\ Áp dụng công thức cosin của góc giữa hai vectơ: \\\\ $\\cos(\\vec{AB}, \\vec{DM}) = \\frac{\\vec{AB} \\cdot \\vec{DM}}{|\\vec{AB}| \\cdot |\\vec{DM}|} = \\frac{\\frac{a^2}{4}}{a \\cdot \\frac{a\\sqrt{3}}{2}} = \\frac{1}{4} \\cdot \\frac{2}{\\sqrt{3}} = \\frac{1}{2\\sqrt{3}} = \\frac{\\sqrt{3}}{6}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: Góc giữa hai vectơ \vec{AM} và \vec{MB} là góc nhọn (Sai vì bằng 90°)[cite: 20]
    vd_da_1_d = "\\True Góc giữa hai vectơ $\\vec{AM}$ và $\\vec{MB}$ bằng $90^\\circ$"
    vd_da_1_s = "Góc giữa hai vectơ $\\vec{AM}$ và $\\vec{MB}$ là góc nhọn"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Vì $ABCD$ là tứ diện đều nên mặt bên $ABC$ là tam giác đều. \\\\ Đoạn thẳng $AM$ là đường trung tuyến của tam giác đều $ABC$ nên đồng thời là đường cao, do đó $AM \\perp BC$. \\\\ Vì điểm $M$ thuộc đoạn thẳng $BC$ nên giá của vectơ $\\vec{MB}$ trùng với đường thẳng $BC$. \\\\ Suy ra hai vectơ $\\vec{AM}$ và $\\vec{MB}$ vuông góc với nhau, tức là: \\\\ $(\\vec{AM}, \\vec{MB}) = 90^\\circ$. \\\\ Vì góc giữa hai vectơ bằng $90^\\circ$ (là góc vuông) nên khẳng định góc giữa hai vectơ là góc nhọn là sai. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: Góc giữa hai vectơ \vec{BA} và \vec{CD} bằng 90°[cite: 20]
    vdc_da_1_d = "\\True Góc giữa hai vectơ $\\vec{BA}$ và $\\vec{CD}$ bằng $90^\\circ$"
    vdc_da_1_s = "Góc giữa hai vectơ $\\vec{BA}$ và $\\vec{CD}$ bằng $60^\\circ$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Ta tính tích vô hướng của hai vectơ $\\vec{BA}$ và $\\vec{CD}$: \\\\ $\\vec{BA} \\cdot \\vec{CD} = \\vec{BA} \\cdot (\\vec{AD} - \\vec{AC}) = \\vec{BA} \\cdot \\vec{AD} - \\vec{BA} \\cdot \\vec{AC}$ \\\\ $= -\\vec{AB} \\cdot \\vec{AD} + \\vec{AB} \\cdot \\vec{AC}$ \\\\ $= -\\left(AB \\cdot AD \\cdot \\cos \\widehat{BAD}\\right) + \\left(AB \\cdot AC \\cdot \\cos \\widehat{BAC}\\right)$. \\\\ Vì tứ diện $ABCD$ đều cạnh $a$ nên các tam giác $ABD$ và $ABC$ là các tam giác đều cạnh $a$, suy ra $\\widehat{BAD} = \\widehat{BAC} = 60^\\circ$. \\\\ Do đó: \\\\ $\\vec{BA} \\cdot \\vec{CD} = -\\left(a \\cdot a \\cdot \\cos 60^\\circ\\right) + \\left(a \\cdot a \\cdot \\cos 60^\\circ\\right) = -\\frac{a^2}{2} + \\frac{a^2}{2} = 0$. \\\\ Vì tích vô hướng $\\vec{BA} \\cdot \\vec{CD} = 0$ nên hai vectơ $\\vec{BA}$ và $\\vec{CD}$ vuông góc với nhau: \\\\ $(\\vec{BA}, \\vec{CD}) = 90^\\circ$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vdc_da_1 else "sai")
    )
    
    list_vdc_2 = [loigiai_vdc_1]
    
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))
    random.shuffle(combined_vdc)
    shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
    
    
    def count_true_answers(answers):
        return sum("\\True" in ans for ans in answers)
    
    
    # Lặp đến khi đáp án có từ 1 đến 3 câu đúng
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
    
    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    content = (
        "\\begin{minipage}{\\textwidth} \n"
        "\\begin{ex}\n"
        + str(noidungcauhoi)
        + "\n"
        "\\choiceTFn \n"
        "{" + str(shuffled_answers_nb[0]) + "}\n"
        "{" + str(shuffled_answers_th[0]) + "}\n"
        "{" + str(shuffled_answers_vd[0]) + "}\n"
        "{" + str(shuffled_answers_vdc[0]) + "}\n"
        "\\loigiai{ \n"
        "\\begin{enumEX}[a)]{1} \n"
        "\\item " + str(shuffled_solutions_nb[0]) + "\n"
        "\\item " + str(shuffled_solutions_th[0]) + "\n"
        "\\item " + str(shuffled_solutions_vd[0]) + "\n"
        "\\item " + str(shuffled_solutions_vdc[0]) + "\n"
        "\\end{enumEX}} \n"
        "\\end{ex}\n \\end{minipage}\n\n" )
    return content
    