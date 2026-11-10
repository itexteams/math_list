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


def bt_dang29_p2_b1_c1_hh12(self):
    # Hàm phụ trợ biểu diễn phân số sang dạng LaTeX chuẩn
    def format_fraction_latex(numerator, denominator):
        val = Rational(numerator, denominator)
        if val.q == 1:
            return str(val.p)
        if val.p < 0:
            return "-\\frac{%s}{%s}" % (-val.p, val.q)
        return "\\frac{%s}{%s}" % (val.p, val.q)
    
    
    # Mã vẽ TikZ hình chóp S.ABCD đáy hình bình hành tâm O, G trên SO chính xác 100% như ảnh[cite: 20]
    # Chú ý: Tuyệt đối không dùng ký hiệu % comment bên trong string để tránh lỗi format string
    tikz_figure = """\\begin{center}
    \\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
    \\coordinate (A) at (0,0);
    \\coordinate (B) at (-1.3,-1.3);
    \\coordinate (C) at (1.4,-1.3);
    \\coordinate (D) at ($(A)+(C)-(B)$);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (S) at ($(O)+(0,2.8)$);
    \\coordinate (G) at ($(S)!0.8!(O)$);
    \\draw[line width=1pt] (S)--(B)--(C)--(D)--(S)--(C);
    \\draw[line width=1pt, dashed] (S)--(A)--(B) (A)--(D) (A)--(C) (B)--(D) (S)--(O);
    \\fill (A) circle (1pt) node[left] {$A$};
    \\fill (B) circle (1pt) node[below left] {$B$};
    \\fill (C) circle (1pt) node[below] {$C$};
    \\fill (D) circle (1pt) node[above right] {$D$};
    \\fill (S) circle (1pt) node[above] {$S$};
    \\fill (O) circle (1pt) node[below] {$O$};
    \\fill (G) circle (1pt) node[left] {$G$};
    \\end{tikzpicture}
    \\end{center}"""
    
    
    
    # Nội dung câu hỏi[cite: 20]
    noidungcauhoi = (
        """Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành tâm $O$. Gọi $G$ là điểm thỏa mãn $\\vec{GS} + \\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$. %s"""
        % (tikz_figure)
    )
    
    ################################################################################ Nhận biết ##############################################
    # Mệnh đề a: Tổng các vectơ cạnh đáy liên tiếp[cite: 20]
    nb_da_1_d = "\\True $\\vec{AB} + \\vec{BC} + \\vec{CD} + \\vec{DA} = \\vec{0}$"
    nb_da_1_s = "$\\vec{AB} + \\vec{BC} + \\vec{CD} + \\vec{DA} = \\vec{SO}$"
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)
    
    list_nb_1 = [nb_da_1]
    
    loigiai_nb_1 = (
        """Áp dụng quy tắc cộng nhiều vectơ liên tiếp, ta có: \\\\ $\\vec{AB} + \\vec{BC} + \\vec{CD} + \\vec{DA} = (\\vec{AB} + \\vec{BC}) + (\\vec{CD} + \\vec{DA}) = \\vec{AC} + \\vec{CA} = \\vec{AA} = \\vec{0}$. \\\\ Do $\\vec{SO} \\neq \\vec{0}$ nên mệnh đề $\\vec{AB} + \\vec{BC} + \\vec{CD} + \\vec{DA} = \\vec{SO}$ là sai. \\\\ Vì vậy mệnh đề là %s."""
        % ("đúng" if "\\True" in nb_da_1 else "sai")
    )
    
    list_nb_2 = [loigiai_nb_1]
    
    combined_nb = list(zip(list_nb_1, list_nb_2))
    random.shuffle(combined_nb)
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
    
    ################################################################################ Thông hiểu ##############################################
    # Mệnh đề b: \vec{OA} + \vec{OB} + \vec{OC} + \vec{OD} = \vec{0}[cite: 20]
    th_da_1_d = "\\True $\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD} = \\vec{0}$"
    th_da_1_s = "$\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD} = 2\\vec{SO}$"
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)
    
    list_th_1 = [th_da_1]
    
    loigiai_th_1 = (
        """Vì $O$ là giao điểm hai đường chéo của hình bình hành $ABCD$ nên $O$ là trung điểm của $AC$ và $O$ là trung điểm của $BD$. \\\\ Theo tính chất trung điểm, ta có: \\\\ $\\bullet$ $\\vec{OA} + \\vec{OC} = \\vec{0}$. \\\\ $\\bullet$ $\\vec{OB} + \\vec{OD} = \\vec{0}$. \\\\ Cộng vế theo vế hai đẳng thức trên, ta được: \\\\ $\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD} = (\\vec{OA} + \\vec{OC}) + (\\vec{OB} + \\vec{OD}) = \\vec{0} + \\vec{0} = \\vec{0}$. \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in th_da_1 else "sai")
    )
    
    list_th_2 = [loigiai_th_1]
    
    combined_th = list(zip(list_th_1, list_th_2))
    random.shuffle(combined_th)
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
    
    ################################################################################ Vận dụng ##############################################
    # Mệnh đề c: \vec{SB} + \vec{SD} = \vec{SA} + \vec{SC}[cite: 20]
    vd_da_1_d = "\\True $\\vec{SB} + \\vec{SD} = \\vec{SA} + \\vec{SC}$"
    vd_da_1_s = "$\\vec{SB} + \\vec{SD} = \\vec{SA} - \\vec{SC}$"
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)
    
    list_vd_1 = [vd_da_1]
    
    loigiai_vd_1 = (
        """Áp dụng quy tắc trung điểm với điểm $S$ bất kỳ: \\\\ $\\bullet$ Vì $O$ là trung điểm của đoạn thẳng $BD$ nên $\\vec{SB} + \\vec{SD} = 2\\vec{SO}$. \\\\ $\\bullet$ Vì $O$ là trung điểm của đoạn thẳng $AC$ nên $\\vec{SA} + \\vec{SC} = 2\\vec{SO}$. \\\\ Từ hai kết quả trên, ta suy ra: \\\\ $\\vec{SB} + \\vec{SD} = \\vec{SA} + \\vec{SC}$ (vì cùng bằng $2\\vec{SO}$). \\\\ Do đó mệnh đề là %s."""
        % ("đúng" if "\\True" in vd_da_1 else "sai")
    )
    
    list_vd_2 = [loigiai_vd_1]
    
    combined_vd = list(zip(list_vd_1, list_vd_2))
    random.shuffle(combined_vd)
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
    
    ################################################################################ Vận dụng cao ##############################################
    # Mệnh đề d: \vec{GS} = 4\vec{OG} (đúng) hoặc \vec{GS} = 3\vec{OG} (sai)[cite: 20]
    vdc_da_1_d = "\\True $\\vec{GS} = 4\\vec{OG}$"
    vdc_da_1_s = "$\\vec{GS} = 3\\vec{OG}$"
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)
    
    list_vdc_1 = [vdc_da_1]
    
    loigiai_vdc_1 = (
        """Theo giả thiết, điểm $G$ thỏa mãn: \\\\ $\\vec{GS} + \\vec{GA} + \\vec{GB} + \\vec{GC} + \\vec{GD} = \\vec{0}$. \\\\ Chèn điểm $O$ vào các vectơ, ta được: \\\\ $(\\vec{GO} + \\vec{OS}) + (\\vec{GO} + \\vec{OA}) + (\\vec{GO} + \\vec{OB}) + (\\vec{GO} + \\vec{OC}) + (\\vec{GO} + \\vec{OD}) = \\vec{0}$ \\\\ $\\Leftrightarrow 5\\vec{GO} + \\vec{OS} + (\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD}) = \\vec{0}$. \\\\ Theo kết quả ở câu b, $\\vec{OA} + \\vec{OB} + \\vec{OC} + \\vec{OD} = \\vec{0}$, do đó: \\\\ $5\\vec{GO} + \\vec{OS} = \\vec{0} \\Leftrightarrow 5\\vec{GO} + (\\vec{GS} - \\vec{GO}) = \\vec{0}$ \\\\ $\\Leftrightarrow \\vec{GS} + 4\\vec{GO} = \\vec{0} \\Leftrightarrow \\vec{GS} = -4\\vec{GO} = 4\\vec{OG}$. \\\\ Do hệ số đúng là $4$ nên mệnh đề $\\vec{GS} = 3\\vec{OG}$ là sai. \\\\ Vì vậy mệnh đề là %s."""
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
        "\\end{ex}\n \\end{minipage}\n\n")
    return content
    