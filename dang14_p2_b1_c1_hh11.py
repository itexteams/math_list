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


def bt_dang14_p2_b1_c1_hh11(self):
    # Khai báo biến (Random tên các điểm để tạo nhiều mã bài)
    ptM = random.choice(['M', 'P', 'Q'])
    ptI = random.choice(['I', 'K', 'H'])
    ptE = random.choice(['E', 'F', 'R'])
    ptN = random.choice(['N', 'J', 'L'])

    # Tách riêng hình vẽ thành biến hinhve
    hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]
    \\coordinate (A) at (1,2);
    \\coordinate (B) at (-1,0);
    \\coordinate (C) at (4,0);
    \\coordinate (D) at (6,2);
    \\coordinate (S) at (2,6);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (M) at ($(S)!0.5!(C)$);
    \\coordinate (I) at ($(S)!0.6667!(O)$);

    \\draw[dashed] (A)--(B) (A)--(D) (S)--(A) (A)--(C) (B)--(D) (S)--(O) (A)--(M);
    \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D);

    \\fill (S) circle (1.5pt) node[above] {$S$};
    \\fill (A) circle (1.5pt) node[left] {$A$};
    \\fill (B) circle (1.5pt) node[below left] {$B$};
    \\fill (C) circle (1.5pt) node[below right] {$C$};
    \\fill (D) circle (1.5pt) node[right] {$D$};
    \\fill (O) circle (1.5pt) node[below] {$O$};
    \\fill (M) circle (1.5pt) node[right] {$%s$};
    \\fill (I) circle (1.5pt) node[left] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (ptM, ptI))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy là hình bình hành. Gọi $%s$ là trung điểm của $SC$. Gọi $%s$ là giao điểm của đường thẳng $A%s$ và mặt phẳng $(SBD)$. Gọi $O$ là giao điểm của $AC$ và $BD$. Khi đó:'''                  
                     % (ptM, ptI, ptM))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True $A%s \\cap SO = %s$' % (ptM, ptI)
    nb_da_1_s = '$A%s \\cap SB = %s$' % (ptM, ptI)
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $O \\in AC \\subset (SAC)$ và $O \\in BD \\subset (SBD)$.\\\\
    Lại có $S \\in (SAC) \\cap (SBD)$.\\\\
    Suy ra $(SAC) \\cap (SBD) = SO$.\\\\
    Trong mặt phẳng $(SAC)$, gọi $%s' = A%s \\cap SO$. Ta có $%s' \\in SO \\subset (SBD)$ nên $%s' \\in (SBD)$.\\\\
    Mặt khác $%s' \\in A%s$.\\\\
    Vậy $%s' = A%s \\cap (SBD) \\Rightarrow %s' \\equiv %s$.\\\\
    Do đó $A%s \\cap SO = %s$.'''
               % (ptI, ptM, ptI, ptI, ptI, ptM, ptI, ptM, ptI, ptI, ptM, ptI))

    # Đưa các lời giải vào danh sách lời giải
    list_nb_2 = [loigiai_nb_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_nb = list(zip(list_nb_1, list_nb_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_nb)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

    ########################################################################
    # Thông hiểu ############################################
    # Các đáp án
    th_da_1_d = '\\True $%sA = 2%s%s$' % (ptI, ptI, ptM)
    th_da_1_s = '$%sA = 3%s%s$' % (ptI, ptI, ptM)
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Xét tam giác $SAC$ có $O$ là trung điểm $AC$ (do $ABCD$ là hình bình hành) và $%s$ là trung điểm $SC$.\\\\
    Suy ra $SO$ và $A%s$ là hai đường trung tuyến của tam giác $SAC$.\\\\
    Theo chứng minh trên, $%s = A%s \\cap SO$, nên $%s$ là trọng tâm của tam giác $SAC$.\\\\
    Suy ra $%sA = 2%s%s$.'''
               % (ptM, ptM, ptI, ptM, ptI, ptI, ptI, ptM))

    # Đưa các lời giải vào danh sách lời giải
    list_th_2 = [loigiai_th_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_th = list(zip(list_th_1, list_th_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_th)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

    ######################################################################## 
    # Vận dụng ############################################
    # Các đáp án
    vd_da_1_d = '\\True Giao điểm $%s$ của đường thẳng $SD$ và mặt phẳng $(AB%s)$ là điểm thuộc đường thẳng $B%s$' % (ptE, ptM, ptI)
    vd_da_1_s = 'Giao điểm $%s$ của đường thẳng $SD$ và mặt phẳng $(AB%s)$ là điểm thuộc đường thẳng $A%s$' % (ptE, ptM, ptI)
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Ta có $%s \\in A%s \\subset (AB%s)$ và $B \\in (AB%s)$ nên đường thẳng $B%s \\subset (AB%s)$.\\\\
    Mặt khác, $%s \\in SO \\subset (SBD)$ và $B \\in (SBD)$ nên đường thẳng $B%s \\subset (SBD)$.\\\\
    Trong mặt phẳng $(SBD)$, gọi $%s = B%s \\cap SD$.\\\\
    Vì $%s \\in B%s \\subset (AB%s)$ nên $%s \\in (AB%s)$.\\\\
    Lại có $%s \\in SD$.\\\\
    Suy ra $%s = SD \\cap (AB%s)$.\\\\
    Vậy giao điểm $%s$ của đường thẳng $SD$ và mặt phẳng $(AB%s)$ thuộc đường thẳng $B%s$.'''  
               % (ptI, ptM, ptM, ptM, ptI, ptM, ptI, ptI, ptE, ptI, ptE, ptI, ptM, ptE, ptM, ptE, ptE, ptM, ptE, ptM, ptI))

    # Đưa các lời giải vào danh sách lời giải
    list_vd_2 = [loigiai_vd_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vd = list(zip(list_vd_1, list_vd_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vd)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
    shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

    ######################################################################## 
    # Vận dụng cao ############################################
    # Các đáp án
    vdc_da_1_d = '\\True Gọi $%s$ là một điểm tuỳ ý trên cạnh $AB$. Khi đó giao điểm của đường thẳng $%s%s$ và mặt phẳng $(SBD)$ là điểm thuộc giao tuyến của hai mặt phẳng $(SBD)$ và $(S%sC)$' % (ptN, ptM, ptN, ptN)
    vdc_da_1_s = 'Gọi $%s$ là một điểm tuỳ ý trên cạnh $AB$. Khi đó giao điểm của đường thẳng $%s%s$ và mặt phẳng $(SBD)$ là điểm thuộc giao tuyến của hai mặt phẳng $(SBD)$ và $(SAB)$' % (ptN, ptM, ptN)
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Gọi $K = %s%s \\cap (SBD)$. Ta có $K \\in %s%s$ và $K \\in (SBD)$.\\\\
    Mặt khác, $%s \\in SC \\subset (S%sC)$ và $%s \\in AB \\subset (S%sC)$ nên đường thẳng $%s%s \\subset (S%sC)$.\\\\
    Do đó, $K \\in %s%s \\subset (S%sC)$ suy ra $K \\in (S%sC)$.\\\\
    Như vậy $K \\in (SBD) \\cap (S%sC)$.\\\\
    Vậy giao điểm của đường thẳng $%s%s$ và mặt phẳng $(SBD)$ là điểm thuộc giao tuyến của hai mặt phẳng $(SBD)$ và $(S%sC)$.'''
               % (ptM, ptN, ptM, ptN, ptM, ptN, ptN, ptN, ptM, ptN, ptN, ptM, ptN, ptN, ptN, ptN, ptM, ptN, ptN))

    # Đưa các lời giải vào danh sách lời giải
    list_vdc_2 = [loigiai_vdc_1]

    # Kết hợp các đáp án và lời giải vào cùng một danh sách
    combined_vdc = list(zip(list_vdc_1, list_vdc_2))

    # Xáo trộn danh sách kết hợp
    random.shuffle(combined_vdc)

    # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
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

    # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
    # Gọi biến hinhve ở đầu phần loigiai
    content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+
        str(noidungcauhoi)+ 
        '\n\\choiceTFn \n'
       '{'+str(shuffled_answers_nb[0])+'}\n'
       '{'+str(shuffled_answers_th[0])+'}\n'
       '{'+str(shuffled_answers_vd[0])+'}\n'
       '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        + str(hinhve) + '\n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n\\end{minipage} \n\n')
    return content

