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


def bt_dang17_p2_b1_c1_hh11(self):
    # Khai báo biến (Random tên các điểm để tạo nhiều mã bài)
    ptM = random.choice(['M', 'E', 'H'])
    ptN = random.choice(['N', 'F', 'K'])
    ptI = random.choice(['I', 'J', 'G'])

    # Tách riêng hình vẽ thành biến hinhve
    hinhve = ('''\\begin{center}
    \\begin{tikzpicture}[scale=0.8, line join=round, line cap=round, line width=1pt]
    \\coordinate (A) at (1,2);
    \\coordinate (B) at (-1,0);
    \\coordinate (C) at (4,0);
    \\coordinate (D) at (6,2);
    \\coordinate (S) at (2,6);
    \\coordinate (O) at ($(A)!0.5!(C)$);
    \\coordinate (M) at ($(S)!0.5!(A)$);
    \\coordinate (N) at ($(S)!0.5!(B)$);
    \\coordinate (I) at (intersection of S--O and M--C);
    \\draw[dashed] (A)--(B) (A)--(D) (S)--(A) (A)--(C) (B)--(D) (S)--(O) (M)--(C) (M)--(D) (N)--(D);
    \\draw (S)--(B) (S)--(C) (S)--(D) (B)--(C)--(D) (M)--(N) (N)--(C) ;
    \\fill (S) circle (1.5pt) node[above] {$S$};
    \\fill (A) circle (1.5pt) node[left] {$A$};
    \\fill (B) circle (1.5pt) node[below left] {$B$};
    \\fill (C) circle (1.5pt) node[below right] {$C$};
    \\fill (D) circle (1.5pt) node[right] {$D$};
    \\fill (O) circle (1.5pt) node[below] {$O$};
    \\fill (M) circle (1.5pt) node[left] {$%s$};
    \\fill (N) circle (1.5pt) node[left] {$%s$};
    \\fill (I) circle (1.5pt) node[above right] {$%s$};
    \\end{tikzpicture}
    \\end{center}''' % (ptM, ptN, ptI))

    # Nội dung câu hỏi
    noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Gọi $%s, %s$ lần lượt là trung điểm của $SA, SB$, $O$ là giao điểm của $AC$ và $BD$.'''                  
                     % (ptM, ptN))

    ########################################################################
    # Nhận biết ############################################
    # Các đáp án
    nb_da_1_d = '\\True Giao điểm của đường thẳng $SA$ và $(ABCD)$ là điểm $A$'
    nb_da_1_s = 'Giao điểm của đường thẳng $SA$ và $(ABCD)$ là điểm $D$'
    list_nb_da_1=[nb_da_1_d,nb_da_1_s]
    nb_da_1=random.choice(list_nb_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_nb_1 = [nb_da_1]

    # Nội dung lời giải
    loigiai_nb_1 = ('''Ta có $A \\in SA$ và $A \\in (ABCD)$.\\\\
    Do đó, giao điểm của đường thẳng $SA$ và mặt phẳng $(ABCD)$ là điểm $A$.'''
               )

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
    th_da_1_d = '\\True Giao điểm của đường thẳng $BD$ và $(SAC)$ là trung điểm của đoạn thẳng $AC$'
    th_da_1_s = 'Giao điểm của đường thẳng $BD$ và $(SAC)$ là trung điểm của đoạn thẳng $AB$'
    list_th_da_1=[th_da_1_d,th_da_1_s]
    th_da_1=random.choice(list_th_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_th_1 = [th_da_1]

    # Nội dung lời giải
    loigiai_th_1 = ('''Trong mặt phẳng $(ABCD)$, gọi $O = AC \\cap BD$.\\\\
    Vì $O \\in BD$ và $O \\in AC \\subset (SAC)$ nên $O = BD \\cap (SAC)$.\\\\
    Do $ABCD$ là hình bình hành nên $O$ là trung điểm của đoạn thẳng $AC$.\\\\
    Vậy giao điểm của đường thẳng $BD$ và $(SAC)$ là trung điểm của đoạn thẳng $AC$.'''
               )

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
    vd_da_1_d = '\\True Giao điểm của đường thẳng $SO$ và $(AB%s%s)$ là điểm $S$' % (ptN, ptM)
    vd_da_1_s = 'Giao điểm của đường thẳng $SO$ và $(AB%s%s)$ là điểm $D$' % (ptN, ptM)
    list_vd_da_1=[vd_da_1_d,vd_da_1_s]
    vd_da_1=random.choice(list_vd_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vd_1 = [vd_da_1]

    # Nội dung lời giải
    loigiai_vd_1 = ('''Vì $%s \\in SA$, $%s \\in SB$ nên mặt phẳng $(AB%s%s)$ chính là mặt phẳng $(SAB)$.\\\\
    Ta có $S \\in SO$ và $S \\in (SAB)$.\\\\
    Mặt khác, $O \\notin (SAB)$ nên $SO$ cắt $(SAB)$ tại $S$.\\\\
    Vậy giao điểm của đường thẳng $SO$ và $(AB%s%s)$ là điểm $S$.'''
               % (ptM, ptN, ptN, ptM, ptN, ptM))

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
    vdc_da_1_d = '\\True Gọi $%s$ là giao điểm của $SO$ và mặt phẳng $(%s%sCD)$. Khi đó $S%s = 2%sO$' % (ptI, ptM, ptN, ptI, ptI)
    vdc_da_1_s = 'Gọi $%s$ là giao điểm của $SO$ và mặt phẳng $(%s%sCD)$. Khi đó $S%s = %sO$' % (ptI, ptM, ptN, ptI, ptI)
    list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
    vdc_da_1=random.choice(list_vdc_da_1)

    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
    list_vdc_1 = [vdc_da_1]

    # Nội dung lời giải
    loigiai_vdc_1 = ('''Trong mặt phẳng $(SAC)$, gọi $%s = SO \\cap %sC$.\\\\
    Vì $%s \\in %sC \\subset (%s%sCD)$ nên $%s \\in (%s%sCD)$.\\\\
    Do đó $%s = SO \\cap (%s%sCD)$.\\\\
    Xét tam giác $SAC$, có $SO$ là đường trung tuyến (do $O$ là trung điểm $AC$) và $%sC$ là đường trung tuyến (do $%s$ là trung điểm $SA$).\\\\
    Do đó $%s$ là trọng tâm của tam giác $SAC$.\\\\
    Theo tính chất trọng tâm, ta có $S%s = 2%sO$.'''
               % (ptI, ptM, ptI, ptM, ptM, ptN, ptI, ptM, ptN, ptI, ptM, ptN, ptM, ptM, ptI, ptI, ptI))

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

