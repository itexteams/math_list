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


def bt_dang4_p2_b3_c1_hh11(self):
        # ==================== KHAI BÁO THÔNG SỐ VÀ RANDOM ====================
        # Đề bài cho AD = k * AM với k = 3
        # Random hệ số k hoặc giữ k = 3 để bảo toàn tính song song của hình học
        k = 3
        dm_over_da = Rational(k - 1, k)      # 2/3
        dn_over_db = Rational(2, 3)          # N là trọng tâm tam giác ABC => BN/BO = 2/3 => DN/DB = 2/3
        
        # ==================== HÌNH VẼ TIKZ ====================
        # Hình vẽ đúng 100% theo mẫu, nét vẽ 1pt, điểm 1pt, màu black
        tikz_figure = ('''\\begin{center}
\\begin{tikzpicture}[scale=1, font=\\footnotesize, line join=round, line cap=round, >=stealth]
\\coordinate (A) at (0,0);
\\coordinate (B) at (-2,-1.6);
\\coordinate (C) at (2.4,-1.6);
\\coordinate (D) at (4.4,0);
\\coordinate (S) at (0.7,3);
\\coordinate (M) at ($(A)!0.333!(D)$);
\\coordinate (P) at ($(A)!0.5!(B)$);
\\coordinate (O) at (intersection of A--C and B--D);
\\coordinate (N) at ($(B)!0.667!(O)$);
\\coordinate (G) at ($(S)!0.667!(P)$);
\\coordinate (X1) at ($(S)!1.5!(S)-(1.6,1)$);
\\coordinate (X2) at ($(S)!1.5!(S)+(1.6,1)$);
\\draw[line width=1pt] (S)--(B) (S)--(C) (S)--(D) (B)--(C) (C)--(D) (X1)--(X2);
\\draw[line width=1pt, dashed] (S)--(A) (A)--(B) (A)--(D) (A)--(C) (B)--(D) (M)--(N) (S)--(P) (C)--(P) (S)--(O) (S)--(N) (P)--(N) (A)--(N) (N)--(D);
\\fill (A) circle (1pt) node[above left] {$A$};
\\fill (B) circle (1pt) node[below left] {$B$};
\\fill (C) circle (1pt) node[below right] {$C$};
\\fill (D) circle (1pt) node[right] {$D$};
\\fill (S) circle (1pt) node[above] {$S$};
\\fill (M) circle (1pt) node[above] {$M$};
\\fill (N) circle (1pt) node[below] {$N$};
\\fill (P) circle (1pt) node[left] {$P$};
\\fill (O) circle (1pt) node[below] {$O$};
\\fill (G) circle (1pt) node[above right] {$G$};
\\node at ($(X1)!0.5!(S)+(0,0.25)$) {$x$};
\\end{tikzpicture}
\\end{center}''')
        
        # ==================== NỘI DUNG CÂU HỎI ====================
        noidungcauhoi = ('''Cho hình chóp $S.ABCD$ có đáy $ABCD$ là hình bình hành. Lấy điểm $M$ trên cạnh $AD$ sao cho $AD = %s AM$. Gọi $G, N$ theo thứ tự là trọng tâm các tam giác $SAB, ABC$.''' % (latex(k)))
        
        ########################################################################
        # Nhận biết 
        ########################################################################
        
        # Các đáp án
        nb_da_1_d = '\\True Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là đường thẳng đi qua $S$ và song song với $AB, CD$'
        nb_da_1_s = 'Giao tuyến của hai mặt phẳng $(SAB)$ và $(SCD)$ là đường thẳng đi qua $S$ và song song với $AC, BD$'
        list_nb_da_1=[nb_da_1_d,nb_da_1_s]
        nb_da_1=random.choice(list_nb_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_nb_1 = [nb_da_1]
        
        # Nội dung lời giải
        loigiai_nb_1 = ('''Ta có: \\\\ $\\begin{cases} S \\in (SAB) \\cap (SCD) \\\\ AB // CD \\\\ AB \\subset (SAB), CD \\subset (SCD) \\end{cases} \\Rightarrow (SAB) \\cap (SCD) = Sx$ (với đường thẳng $Sx$ đi qua $S$ và $Sx // AB // CD$).''')
        
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
        th_da_1_d = '\\True $\\dfrac{DN}{DB} = %s$' % (latex(dn_over_db))
        th_da_1_s = '$\\dfrac{DN}{DB} = %s$' % (latex(Rational(1, 3)))
        list_th_da_1=[th_da_1_d,th_da_1_s]
        th_da_1=random.choice(list_th_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_th_1 = [th_da_1]
        
        # Nội dung lời giải
        loigiai_th_1 = ('''Gọi $O$ là tâm hình bình hành $ABCD$. \\\\ Vì $N$ là trọng tâm của tam giác $ABC$ nên $BN = \\dfrac{2}{3} BO = \\dfrac{2}{3} \\cdot \\dfrac{1}{2} BD = \\dfrac{1}{3} BD \\Rightarrow \\dfrac{DN}{DB} = %s$.''' % (latex(dn_over_db)))
        
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
        vd_da_1_d = '\\True $MN$ song song với mặt phẳng $(SCD)$'
        vd_da_1_s = '$MN$ cắt với mặt phẳng $(SCD)$'
        list_vd_da_1=[vd_da_1_d,vd_da_1_s]
        vd_da_1=random.choice(list_vd_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vd_1 = [vd_da_1]
        
        # Nội dung lời giải
        loigiai_vd_1 = ('''Mặt khác, ta có $AD = %s AM \\Rightarrow \\dfrac{DM}{DA} = %s$. \\\\ Xét tam giác $ADB$, ta có $\\dfrac{DM}{DA} = \\dfrac{DN}{DB} = %s$ nên $MN // AB \\Rightarrow MN // CD$. \\\\ Mà $CD \\subset (SCD)$ nên $MN // (SCD)$.''' % (latex(k), latex(dm_over_da), latex(dn_over_db)))
        
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
        vdc_da_1_d = '\\True $NG$ song song với mặt phẳng $(SAC)$'
        vdc_da_1_s = '$NG$ cắt với mặt phẳng $(SAC)$'
        list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
        vdc_da_1=random.choice(list_vdc_da_1)
        
        # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
        list_vdc_1 = [vdc_da_1]
        
        # Nội dung lời giải
        loigiai_vdc_1 = ('''Gọi $P$ là trung điểm $AB$. \\\\ Tam giác $SPC$ có: $\\dfrac{PG}{PS} = \\dfrac{PN}{PC} = \\dfrac{1}{3}$ (tính chất trọng tâm). \\\\ Suy ra $NG // SC$. \\\\ Mà $SC \\subset (SAC)$ nên $NG // (SAC)$.''')
        
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