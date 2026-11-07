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


def bt_dang5_p2_b3_c1_hh11(self):
        # ==================== HÌNH VẼ TIKZ ====================
        # Cập nhật: Hai đoạn khoanh đỏ (thuộc đường t và đường y nằm khuất bên trong) chuyển thành nét đứt
        tikz_figure = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (-2.2,-1.8);
\\coordinate (C) at (2.4,-1.8);
\\coordinate (D) at (4.6,0);
\\coordinate (S) at (0.7,3.2);
\\coordinate (M) at ($(S)!0.5!(A)$);
\\coordinate (E) at ($(A)!0.5!(B)$);
\\coordinate (F) at ($(B)!0.5!(C)$);
\\coordinate (X1) at ($(S)-(3.2,2.0)$);
\\coordinate (X2) at ($(S)+(1.6,1.0)$);
\\coordinate (Y1) at ($(M)-(3.0,0)$);
\\coordinate (Y2) at ($(M)+(4.5,0)$);
\\coordinate (T1) at ($(M)-(3.0,-1.6)$);
\\coordinate (T2) at ($(M)+(4.5,-2.4)$);
\\coordinate (T_SB) at (intersection of T1--T2 and S--B);
\\coordinate (T_SC) at (intersection of T1--T2 and S--C);
\\coordinate (Y_SC) at (intersection of Y1--Y2 and S--C);
\\draw[line width=1pt] (X1)--(X2) (T1)--(T_SB) (T_SC)--(T2) (Y1)--(M) (Y_SC)--(Y2);
\\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D);
\\draw[line width=1pt, dashed] (T_SB)--(M) (M)--(T_SC) (M)--(Y_SC) (S)--(A) (A)--(B) (A)--(D) (A)--(C) (M)--(E) (M)--(F) (E)--(F) (A)--(F) (M)--(C) (M)--(B);
\\fill (A) circle (1pt) node[left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (S) circle (1pt) node[above] {$S$};
\\fill (M) circle (1pt) node[above right] {$M$};
\\fill (E) circle (1pt) node[below left] {$E$};
\\fill (F) circle (1pt) node[below] {$F$};
\\node at ($(X2)+(-0.3,0.2)$) {$x$};
\\node at ($(Y2)+(-0.8,0.25)$) {$y$};
\\node at ($(T2)+(-2.4,1.5)$) {$t$};
\\end{tikzpicture}
\\end{center}''')
        
        # Khai báo biến
        ten_hinh = "S.ABCD"
        
        # Nội dung câu hỏi
        noidungcauhoi = ('''Cho hình chóp $%s$ có đáy là hình bình hành. Điểm $M$ thuộc cạnh $SA$, điểm $E$ và $F$ lần lượt là trung điểm của $AB$ và $BC$. Khi đó:''' % (ten_hinh))
        
        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '\\True $EF // AC$'
        nb_da_1_s = '$EF // BD$'
        list_nb_da_1=[nb_da_1_d,nb_da_1_s]
        nb_da_1=random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Trong tam giác $ABC$, vì $E$ là trung điểm của $AB$ và $F$ là trung điểm của $BC$ nên $EF$ là đường trung bình của tam giác $ABC$. \\\\ Do đó, $EF // AC$.''')
        
        # Đưa các lời giải vào danh sách lời giải
        list_nb_2 = [loigiai_nb_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_nb = list(zip(list_nb_1, list_nb_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_nb)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
        
        ########################################################################
        # Thông hiểu 
        ########################################################################
        
        # Các đáp án
        th_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là đường thẳng qua $S$ và song song với $AB, CD$'
        th_da_1_s = 'Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là đường thẳng qua $S$ và song song với $AC$'
        list_th_da_1=[th_da_1_d,th_da_1_s]
        th_da_1=random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Xác định giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$: \\\\ Ta có: $\\begin{cases} S \\in (SAB) \\cap (SCD) \\\\ AB \\subset (SAB); CD \\subset (SCD) \\\\ AB // CD \\end{cases}$. \\\\ Suy ra $Sx = (SAB) \\cap (SCD)$, với $Sx$ là đường thẳng qua $S$ và $Sx // AB // CD$.''')
        
        # Đưa các lời giải vào danh sách lời giải
        list_th_2 = [loigiai_th_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_th = list(zip(list_th_1, list_th_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_th)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
        
        ########################################################################
        # Vận dụng 
        ########################################################################
        
        # Các đáp án
        vd_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(MBC)$ và $(SAD)$ là đường thẳng qua $M$ và song song với $BC$'
        vd_da_1_s = 'Giao tuyến của hai mặt phẳng $(MBC)$ và $(SAD)$ là đường thẳng qua $M$ và song song với $AB$'
        list_vd_da_1=[vd_da_1_d,vd_da_1_s]
        vd_da_1=random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Xác định giao tuyến của hai mặt phẳng $(MBC)$ và $(SAD)$: \\\\ Ta có: $\\begin{cases} M \\in SA, SA \\subset (SAD) \\\\ M \\in (MBC) \\end{cases} \\Rightarrow M \\in (MBC) \\cap (SAD)$. \\\\ Khi đó: $\\begin{cases} M \\in (MBC) \\cap (SAD) \\\\ BC \\subset (MBC); AD \\subset (SAD) \\\\ BC // AD \\end{cases}$. \\\\ Suy ra $My = (MBC) \\cap (SAD)$, $My$ là đường thẳng qua $M$ và $My // BC // AD$.''')
        
        # Đưa các lời giải vào danh sách lời giải
        list_vd_2 = [loigiai_vd_1]
        
        # Kết hợp các đáp án và lời giải vào cùng một danh sách
        combined_vd = list(zip(list_vd_1, list_vd_2))
        
        # Xáo trộn danh sách kết hợp
        random.shuffle(combined_vd)
        
        # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
        shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
        
        ########################################################################
        # Vận dụng cao 
        ########################################################################
        
        # Các đáp án
        vdc_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(MEF)$ và $(SAC)$ là đường thẳng qua $M$ và song song với $AC$'
        vdc_da_1_s = 'Giao tuyến của hai mặt phẳng $(MEF)$ và $(SAC)$ là đường thẳng qua $M$ và song song với $SC$'
        list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
        vdc_da_1=random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Xác định giao tuyến của hai mặt phẳng $(MEF)$ và $(SAC)$: \\\\ Ta có: $\\begin{cases} M \\in SA, SA \\subset (SAC) \\\\ M \\in (MEF) \\end{cases} \\Rightarrow M \\in (MEF) \\cap (SAC)$. \\\\ Xét tam giác $ABC$, ta có $EF$ là đường trung bình $\\Rightarrow EF // AC$. \\\\ Khi đó: $\\begin{cases} M \\in (MEF) \\cap (SAC) \\\\ EF \\subset (MEF); AC \\subset (SAC) \\\\ EF // AC \\end{cases}$. \\\\ Suy ra $Mt = (MEF) \\cap (SAC)$, $Mt$ là đường thẳng qua $M$ và $Mt // EF // AC$.''')
        
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
        
        # Xuất câu hỏi theo đúng mẫu
        content = ('\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
        '\\choiceTFn \n'
        '{'+str(shuffled_answers_nb[0])+'}\n'
        '{'+str(shuffled_answers_th[0])+'}\n'
        '{'+str(shuffled_answers_vd[0])+'}\n'
        '{'+str(shuffled_answers_vdc[0])+'}\n'
        '\\loigiai{ \n'
        + str(tikz_figure) + '\n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item '+str(shuffled_solutions_nb[0])+'\n'
        '\\item '+str(shuffled_solutions_th[0])+'\n'
        '\\item '+str(shuffled_solutions_vd[0])+'\n'
        '\\item '+str(shuffled_solutions_vdc[0])+'\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n'
        '\\end{minipage}\n\n')
        
        return content